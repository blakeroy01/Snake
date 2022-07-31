package game

import (
	"bytes"
	"fmt"
	"math/rand"
	"net"
	"strconv"
	"time"

	"github.com/blakeroy01/Snake/transport"
	"go.uber.org/zap"
)

var (
	// Games is a map of active games stored by ID. We will need this in order to
	// support threads or lookup a game by ID
	Games map[int]*Game

	// CreateNewGame is a signal for the server to create a new game for players to join into.
	// It is flagged after one game is played
	CreateNewGame = true

	// Auto-incrementing ID's
	PlayerID = 0
	GameID   = 0
)

// Player holds all relevant data for a player in a game
type Player struct {
	ID      int
	Address net.Addr
	X       int
	Y       int
	length  int
	lost    bool
}

// Apple holds all relevant data for an apple in a game
type Apple struct {
	X int
	Y int
}

// Game holds all reelvant data for a game
type Game struct {
	ID      int
	Players map[string]*Player
	Apple   *Apple
	Logger  *zap.Logger
	Size    int
	PIO     []*Player
}

// Setup Functions

// NewGame creates and returns a pointer to a new game without players defined. This should be called from main.
// Default to size 2 for MVP
func NewGame(apple *Apple, logger *zap.Logger) *Game {
	GameID++
	return &Game{
		ID:      GameID,
		Apple:   apple,
		Logger:  logger,
		Size:    2,
		Players: make(map[string]*Player),
		PIO:     make([]*Player, 0),
	}
}

// NewApple creates and returns a pointer to an apple, this should only be called when creating a new game.
func NewApple(x int, y int) *Apple {
	return &Apple{
		X: x,
		Y: y,
	}
}

// Over checks each frame that no players in a game have a true win status.
func (game *Game) Over() bool {
	return false
}

// Join fills the empty player slots for the specified game.
func (game *Game) Join(address net.Addr) {
	PlayerID++
	newPlayer := &Player{
		ID:      PlayerID,
		Address: address,
		X:       rand.Intn(25) + 3, Y: 15,
		length: 1,
		lost:   false,
	}

	game.Players[address.String()] = newPlayer
	game.PIO = append(game.PIO, newPlayer)

	playerAssignBuffer := bytes.Buffer{}
	playerAssignBuffer.WriteString(strconv.Itoa(newPlayer.ID))
	playerAssignBuffer.WriteString("&")
	playerAssignBuffer.WriteString(strconv.Itoa(game.ID))
	_, err := transport.Packet.WriteTo(playerAssignBuffer.Bytes(), address)
	if err != nil {
		game.Logger.Fatal(
			"couldn't write to player",
			zap.ByteString("player buffer: ", playerAssignBuffer.Bytes()),
		)
	}
	game.Logger.Info(
		"player joined",
		zap.Any("Player: ", game.Players[address.String()]),
	)
}

// IsFull is a quick check for game size being reached in a snake game.
// This method returns true if [size] players are present, false otherwise.
func (game *Game) IsFull() bool {
	return len(game.Players) >= game.Size
}

// End sets the specified player's value to true. This should halt all
// Play() functionality

// TODO send data to clients and say game over
func (player *Player) End() {
	player.lost = true
}

func (game *Game) WriteToClient() {
	appleData := game.Apple.String()
	playerData := bytes.NewBufferString("")
	for i := range game.PIO {
		playerData.WriteString(game.PIO[i].String())
		playerData.WriteByte('&')
	}

	for i := range game.Players {
		game.Players[i].ScoreCheck(game.Apple, game.Logger)
		playerBuffer := bytes.Buffer{}
		playerBuffer.WriteString(appleData)
		playerBuffer.WriteByte('&')
		playerBuffer.Write(playerData.Bytes())

		_, err := transport.Packet.WriteTo(playerBuffer.Bytes(), game.Players[i].Address)
		if err != nil {
			game.Logger.Fatal(
				"couldn't write to player",
				zap.ByteString("player buffer: ", playerBuffer.Bytes()),
			)
		}
	}
}

// Play runs while a player has not won in the specfied game.
// Server will update game data such as handling a score, moving snake head.
// Updated game data will be sent to each connection.
func (game *Game) Play() {
	for !game.Over() {
		game.WriteToClient()
		time.Sleep(150 * time.Millisecond)
	}
	game.WriteToClient()
	println("Game over!")
}

// MoveApple checks if the player has scored, and moves the apple if necessary
func (player *Player) ScoreCheck(apple *Apple, logger *zap.Logger) {
}

// MoveUp moves the specified player up
func (player *Player) MoveUp() {
	player.Y--
}

// MoveDown moves the specified player down
func (player *Player) MoveDown() {
	player.Y++
}

// MoveLeft moves the specified player left
func (player *Player) MoveLeft() {
	player.X--
}

// MoveRight moves the specified player right
func (player *Player) MoveRight() {
	player.X++
}

// String turns the specified player data into writable string format
func (player *Player) String() string {
	return fmt.Sprintf(
		"%v&%d&%d&%d&%v",
		player.ID, player.X, player.Y,
		player.length, player.lost,
	)
}

// String turns the specified apple data into writable string format
func (apple *Apple) String() string {
	return fmt.Sprintf(
		"%d&%d",
		apple.X, apple.Y,
	)
}

// GetPlayerByAddress returns the specified pointer to Player
func GetGameByID(id int) *Game {
	return Games[id]
}
