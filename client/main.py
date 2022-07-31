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

    # Get player id
    
    player_id = None
    game_id = None
    if player_id is None:
        playerval = conn.receive()
        player_id, game_id = playerval[0], playerval[1]
        print("ID: " + player_id, "Game ID: " + game_id)
    
    # create our player for frontend
    if int(player_id) % 2 > 0:
        P1 = create_new_player(1,player_id,[])
        P2 = create_new_player(1,None,[])
        local_cache.add_player(P1)
        print(local_cache.PLAYERS)
    else:
        P1 = create_new_player(1,None,[])
        P2 = create_new_player(1,player_id,[])
        local_cache.add_player(P2)
        print(local_cache.PLAYERS)


    MESSAGE = b"d"

    # Game loop
    running = True
    while running:
        # receive data from socket
        server_data = conn.receive()
        print(server_data)
        # No need to update the client image if no data is sent from server
        if server_data[0] is None:
            continue
        
        # SNAK-8 (Comments for instruction)
        # parse data from socket, we have an array that contains this data [appx, appy, player1id, p1x, p1y, p1l, p1lost, player2id, p2x, p2y, p2l, p2lost, _]
        appx, appy, player1id, p1x, p1y, p1l, p1lost, player2id, p2x, p2y, p2l, p2lost, _ = server_data[0], server_data[1], server_data[2], server_data[3], server_data[4], server_data[5], server_data[6], server_data[7], server_data[8], server_data[9],  server_data[10], server_data[11], server_data[12] 
        
        if not P2.id:
            P2.id = player2id
            local_cache.add_player(P2)
        elif not P1.id:
            P1.id = player1id
            local_cache.add_player(P1)


        # Check if any player has lost. In this case we only have player 1 and player 2. So something like: if p1lost = "true", end loop and determine winner.
        if p1lost == "true" or p2lost == "true":
            running = False 
        # Update our stored players with the server data. In our case, we can create two players before the running loop, have them be the only two players in the game for now, then update their attributews with the values we get from the server
        player1 = local_cache.PLAYERS[player1id]  
        player2 = local_cache.PLAYERS[player2id]  
        local_cache.PLAYERS[player1id] = player1.update_player(p1l,(p1x,p1y))
        local_cache.PLAYERS[player2id] = player2.update_player(p1l,(p2x,p2y))
        
                

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
    print("Game Over")
    
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