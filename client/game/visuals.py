import pygame

# Screen setup
(SCREEN_WIDTH, SCREEN_HEIGHT) = (800, 800)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Astronomic Studios: Snake')
pygame.display.flip()

# Color presets

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0) 
# PURPLE = (128, 0, 128)
# ORANGE = (255, 165 ,0)
# TURQUOISE = (64, 224, 208)


# Will serve as a border color
SCREEN.fill(GREY)


# Defined grid variables in case we change SCREEN.
margin = 25
rows_cols = SCREEN_HEIGHT / margin
cell = SCREEN_HEIGHT / rows_cols
border = (2, 31)


# draw_grid draws white squares along the screen, and leaves a border of `margin` pixels
# It then draws outlines to these squares to create a grid visual.
def draw_grid():
    for x in range(0 + margin, SCREEN_WIDTH - margin, margin):
        for y in range(0 + margin, SCREEN_HEIGHT - margin, margin):
            rect = pygame.Rect(x, y, cell, cell)
            pygame.draw.rect(SCREEN, WHITE, rect, 0)

    for x in range(0 + margin, SCREEN_WIDTH - margin, margin):
        for y in range(0 + margin, SCREEN_HEIGHT - margin, margin):
            rect = pygame.Rect(x, y, cell, cell)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


# draw_snakes inputs are the player objects' snakes. For each cell in the snakes,
# it highlights the corresponding grid location. This gives the user a visual of a snake. 
def draw_snakes(player_one_snake, player_two_snake):
    for block in player_one_snake:
        x, y = block
        rect_x = ((x-1) * SCREEN_WIDTH) / rows_cols
        rect_y = ((y-1) * SCREEN_HEIGHT) / rows_cols
        rect = pygame.Rect(rect_x, rect_y, cell, cell)
        pygame.draw.rect(SCREEN, GREEN, rect, 0)

    for block in player_two_snake:
        x, y = block
        rect_x = ((x-1) * SCREEN_WIDTH) / rows_cols
        rect_y = ((y-1) * SCREEN_HEIGHT) / rows_cols
        rect = pygame.Rect(rect_x, rect_y, cell, cell)
        pygame.draw.rect(SCREEN, BLUE, rect, 0)


# draw_apple inputs the position of the apple and blits a red square to grid.
def draw_apple(apple_pos):
    x, y = apple_pos
    rect_x = ((x-1) * SCREEN_WIDTH) / rows_cols
    rect_y = ((y-1) * SCREEN_HEIGHT) / rows_cols
    rect = pygame.Rect(rect_x, rect_y, cell, cell)
    pygame.draw.rect(SCREEN, RED, rect, 0)


def draw_main_menu():
    SCREEN.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 32)
    play_text = font.render("Press enter to start!", True, WHITE)
    text_rect = play_text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    SCREEN.blit(play_text, text_rect)
    pygame.display.update()

def draw_end_menu(won):
    SCREEN.fill(BLACK)
    text = "You lost! Play again?"
    if won:
        text = "You won! Play again?"
    font = pygame.font.Font('freesansbold.ttf', 32)
    play_text = font.render(text, True, WHITE)
    text_rect = play_text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    SCREEN.blit(play_text, text_rect)
    pygame.display.update()