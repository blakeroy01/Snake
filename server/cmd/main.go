package main

import (
	"bytes"
	"os"
	"net"

	"go.uber.org/zap"
)

func main() {

	// UDP connection for games running on this server
	packet, err := net.ListenPacket("udp", ":10000")
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
	createNewGame := true
	for {
		n, playerAddress, err := packet.ReadFrom(data)
		if err != nil {
			logger.Fatal(err.Error())
		}
		logger.Info("PLAYERADDRESS", zap.Any("Player address", playerAddress))

		data = bytes.TrimSpace(data[:n])

		logger.Info("Data received", zap.String("Data", string(data)))

		formattedData := string(data)
		logger.Info("Data", zap.Any("data", formattedData))

		command := data

		// this switch statement allows our server to arbitrate
		switch string(command) {
		case "j":
			if createNewGame {
				// create game
			}
			// join game

			// Handle all packet directions from clients
		case "u":
			// move up

		case "d":
			// move down

		case "l":
			// move left

		case "r":
			// move right

		case "c":
			// collision detected
		default:
		}
	}
}