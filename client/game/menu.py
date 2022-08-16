import pygame
import pygame_menu

start_game = False

menu = pygame_menu.Menu('Welcome', 1200, 800, theme=pygame_menu.themes.THEME_DARK)
how_to_play_menu = pygame_menu.Menu('How To Play', 1200, 800, theme=pygame_menu.themes.THEME_DARK)

how_to_play = 'Enter your name \n' \
        'Press "Play" enter the game \n' \
        'Press "Quit" to close game \n' \
        'Press UP/DOWN/LEFT/RIGHT to move your snake \n' \
        'Have fun!'

how_to_play_menu.add.label(how_to_play, max_char=-1, font_size=20)
how_to_play_menu.add.button('Back', pygame_menu.events.BACK)

menu.add.text_input('Name: ', default='', maxchar=10)
menu.add.button(how_to_play_menu.get_title(), how_to_play_menu)
menu.add.button('Play', start_game = True)
menu.add.button('Quit', pygame_menu.events.EXIT)