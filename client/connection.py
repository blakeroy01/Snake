import socket
import pygame

#initialize socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = ("127.0.0.1", 10000)

 #x&y&length&direction&applex&appley

#sending
def send(data):
    client_socket.sendto(data, destination)

#receiving
def receive():
    try:
        client_socket.settimeout(2)
        data, _ = client_socket.recvfrom(1024)
        return data.decode('utf-8').split('&', -1)
    except socket.timeout:
        pygame.event.get()
        return None, None
        