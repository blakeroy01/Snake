import time
import pygame
import sys
import game.visuals as visuals
import game.cache as local_cache
import connection as conn
from game.player import create_new_player

visuals.initialize_game()

def play():
    # Client joins the server
    MESSAGE = b"j"
    MESSAGE = MESSAGE + b"&" + b"0"
    conn.send(MESSAGE)

    

    local_cache.add_player(player)
    local_cache.add_player(player)
    # Get player id
    player_id = None
    game_id = None
    if player_id is None:
        playerval = conn.receive()
        player_id, game_id = playerval[0], playerval[1]
        print("ID: " + player_id, "Game ID: " + game_id)
    
    # create our player for frontend
    P1 = create_new_player(1,player_id,[])
    P2 = create_new_player(1,None,[])
    


    MESSAGE = b"d"

    # Game loop
    running = True
    while running:
        # receive data from socket
        server_data = conn.receive()
        # No need to update the client image if no data is sent from server
        if server_data is None:
            continue
        
        # SNAK-8 (Comments for instruction)
        # parse data from socket, we have an array that contains this data [appx, appy, player1id, p1x, p1y, p1l, p1lost, player2id, p2x, p2y, p2l, p2lost, _]
        for data in server_data:
            print(data)

        # Check if any player has lost. In this case we only have player 1 and player 2. So something like: if p1lost = "true", end loop and determine winner.

        # Update our stored players with the server data. In our case, we can create two players before the running loop, have them be the only two players in the game for now, then update their attributews with the values we get from the server


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
                running = False
                pygame.quit()
                sys.exit()

        # Border collision detection

        # Fire the set direction through UDP
        conn.send(MESSAGE + b"&" + bytes(game_id, "utf-8"))

        # SNAK-8 
        # Draw our objects onto the screen


        pygame.display.set_caption('Astronomic Studios Snake Game')
        visuals.CLOCK.tick(10)
        pygame.display.update()
        time.sleep(2)
    
    # end game logic

def menu():
    # draw the main menu here
    # send a request to join the game
    return False

def main():
    pygame.init()
    while menu():
        pass
    play()
    conn.client_socket.close()
    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    main()