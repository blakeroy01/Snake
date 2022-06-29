import time
import pygame
import game.visuals as visuals
import game.cache as local_cache
visuals.initialize_game()

def game_loop():
    game_over = False
    X = visuals.WINDOW_WIDTH/2
    Y = visuals.WINDOW_HEIGHT/2

    # local_player = Player(data_from_udp_socket)
    # local_cache.add_player(local_player)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        if X >= visuals.WINDOW_WIDTH or X < 0 or Y >= visuals.WINDOW_HEIGHT or Y < 0:
            game_over = True
        local_cache.display_players()
        pygame.display.update()
        pygame.display.set_caption('Astronomic Studios Snake Game')
        visuals.CLOCK.tick(10)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()

game_loop()