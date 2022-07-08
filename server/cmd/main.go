package main

import (
	"bytes"
	"os"
	"strings"
	"strconv"
	transport "github.com/blakeroy01/Snake/transport"
	game "github.com/blakeroy01/Snake/game"
	"go.uber.org/zap"
)

func main() {
	game.Games = make(map[int]*game.Game)
	// serves as a lobby for players waiting for their game to start
	// in later versions, this should expand into a slice of *game.Game
	var lobby *game.Game

	// UDP connection for games running on this server
	err := transport.Initialize(":10000")
	if err != nil {
		os.Exit(1)
	}

	// Production logging
	logger, err := zap.NewProduction()
	if err != nil {
		os.Exit(1)
	}
	defer logger.Sync()

	logger.Info("UDP Server Started")

	// data is the buffer in which we will store data from the UDP socket
	data := make([]byte, 1024)
	for {
		n, playerAddress, err := transport.Packet.ReadFrom(data)
		if err != nil {
			logger.Fatal(err.Error())
		}

		data = bytes.TrimSpace(data[:n])

		logger.Info("Data received", zap.String("Data", string(data)))

		formattedData := strings.SplitN(string(data), "&", 2)
		logger.Info("Data", zap.Any("data", formattedData))

		command, sGameID := formattedData[0], formattedData[1]
		gameID, err := strconv.Atoi(sGameID)
		if err != nil {
			logger.Fatal(err.Error())
		}

		// this switch statement allows our server to arbitrate
		switch string(command) {
		case "j":
			if game.CreateNewGame {
				lobby = game.NewGame(game.NewApple(15, 15), logger)
				game.Games[lobby.ID] = lobby

				// we now do not need another lobby as there is one finding players
				game.CreateNewGame = false
			}
			// let player join the lobby
			lobby.Join(playerAddress)
			if lobby.IsFull() {
				logger.Info(
					"lobby is full",
					zap.Any("Game: ", lobby),
				)
				// to everyone in the lobby - "go have fun"
				go game.Games[lobby.ID].Play()

				// No lobby present for players to join, we need to create a new one.
				lobby = nil
				game.CreateNewGame = true
			}

			// Handle all packet directions from clients
		case "u":
			foundGame := game.GetGameByID(gameID)
			foundGame.Players[playerAddress.String()].MoveUp()

		case "d":
			foundGame := game.GetGameByID(gameID)
			foundGame.Players[playerAddress.String()].MoveDown()

		case "l":
			foundGame := game.GetGameByID(gameID)
			foundGame.Players[playerAddress.String()].MoveLeft()

		case "r":
			foundGame := game.GetGameByID(gameID)
			foundGame.Players[playerAddress.String()].MoveRight()

		case "c":
			foundGame := game.GetGameByID(gameID)
			foundGame.Players[playerAddress.String()].End()
			logger.Info("collision detected")
		default:
		}
	}
}