package transport

import (
	"net"
)

var Packet net.PacketConn

func Initialize(port string) error {
	packet, err := net.ListenPacket("udp", port)
	if err != nil {
		return err
	}
	Packet = packet
	return nil
}