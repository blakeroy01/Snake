import game
import socket
import sys
import pygame


UDP_IP = "127.0.0.1"
UDP_PORT = 10000
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(message):
    UDPSocket.sendto(message, (UDP_IP, UDP_PORT))

def get():
    try:
        UDPSocket.settimeout(2)
        data, address = UDPSocket.recvfrom(1024)
        return data, address
    except socket.timeout:
        pygame.event.get()
        return None, None


def menu():
    game.draw_main_menu()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return False
            elif event.key == pygame.K_ESCAPE:
                return False
    return True


def play():
    # Client joins the server
    MESSAGE = b"j"
    MESSAGE = MESSAGE + b"&" + b"0"
    send(MESSAGE)


    # create both players for our frontend
    player_1 = game.new_player()
    player_2 = game.new_player()
    
    # Get player assignment (1 or 2)
    player_assignment = None
    game_id = None
    if player_assignment is None:
        playerval, _ = get()
        player_assignment, game_id = playerval.decode("utf-8").split('&', -1)
    
    MESSAGE = b"d"
    WINNER = 0

    # Game loop
    running = True
    while running:
        game.draw_grid()

        # receive data from socket and parse into variables
        data, _ = get()
        if data is None:
            continue
        
        appx, appy, p1x, p1y, p1l, p1lost, p2x, p2y, p2l, p2lost, _ = data.decode("utf-8").split("&", -1)


        # Win/lose code
        if p1lost == "true":
            running = False
            WINNER = 2
            print("Player 1 lost")
        elif p2lost == "true":
            running = False
            WINNER = 1
            print("Player 2 lost")

        # Update our stored player's with the server data
        player_1.update_player((int(p1x), int(p1y)), int(p1l))
        player_2.update_player((int(p2x), int(p2y)), int(p2l))

        # User input will change the direction that is being fired
        # to the server each iteration
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and MESSAGE != b"r":
                    MESSAGE = b"l"

                elif event.key == pygame.K_d and MESSAGE != b"l":
                    MESSAGE = b"r"

                elif event.key == pygame.K_w and MESSAGE != b"d":
                    MESSAGE = b"u"

                elif event.key == pygame.K_s and MESSAGE != b"u":
                    MESSAGE = b"d"

            # Handle a quit
            if event.type == pygame.QUIT:
                UDPSocket.close()
                pygame.quit()
                sys.exit()

        # Border collision detection
        if player_assignment == "1":
            MESSAGE = player_1.border_check(MESSAGE)
            MESSAGE = player_1.collision_check(MESSAGE, player_2)
        else:
            MESSAGE = player_2.border_check(MESSAGE)
            MESSAGE = player_2.collision_check(MESSAGE, player_1)

        # Fire the set direction through UDP
        send(MESSAGE + b"&" + bytes(game_id, "utf-8"))

        # Draw our objects onto the screen
        game.draw_apple(apple_pos=(int(appx), int(appy)))
        game.draw_snakes(player_one_snake=player_1.snake, player_two_snake=player_2.snake)
        pygame.display.update()
    
    end(int(WINNER), int(player_assignment))


def end(winner, localPlayer):
    won = False
    print(winner == localPlayer)
    if winner == localPlayer:
        won = True
    response = False
    while not response:
        game.draw_end_menu(won)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    response = True
                    play()
                elif event.key == pygame.K_ESCAPE:
                    response = True

def main():
    pygame.init()
    while menu():
        pass
    play()
    UDPSocket.close()
    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    main()