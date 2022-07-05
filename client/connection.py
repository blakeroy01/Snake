import socket
import pygame

#initialize socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = ("127.0.0.1", 10000)

 #x&y&length&direction&applex&appley

#sending
def send(data): #data is a string
    encoded_string = data.encode() #convert to bytes
    byte_array = bytearray(encoded_string) #convert to bytearray
    client_socket.sendto(byte_array, destination) #send data to server

#receiving
def receive():
    try:
        client_socket.settimeout(2)
        data, address = client_socket.recvfrom(1024) #receive data from server
        data_string = data.decode('utf-8').strip('\x00') #convert to string
        data_string = data_string.split('&') #split string into list, example below
        # x_pos = int(data_string[0])
        # y_pos = int(data_string[1])
        # length = int(data_string[2])
        # direction = int(data_string[3])
        # apple_x = int(data_string[4])
        # apple_y = int(data_string[5])
        return data_string, address
    except socket.timeout:
        pygame.event.get()
        return None, None
        