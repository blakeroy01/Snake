
from .visuals import border

class Player:
    def __init__(self, snake, length):
        # snake is the frontend defined queue which
        # holds (x,y) coordinates in the desired order
        self.snake = []
        self.snake.append(snake)
        self.length = length

    # update_player pushes the new coordinates fired from the server to the snake
    # updates the length (it will increase on a user score)
    # then pops the tail of the snake if the user did not score
    def update_player(self, head_coordinates, length):
        self.snake.append(head_coordinates)
        self.length = length

        if len(self.snake) >= length + 1:
            self.snake.pop(0)

    def get_head(self):
        return self.snake[self.length-1]

    def border_check(self, MESSAGE):
        player_x, player_y = self.get_head()
        border_min, border_max = border
        if player_x == border_min and MESSAGE == b"l":
            MESSAGE = b"u"
        if player_x == border_max and MESSAGE == b"r":
            MESSAGE = b"d"
        if player_y == border_min and MESSAGE == b"u":
            MESSAGE = b"r"
        if player_y == border_max and MESSAGE == b"d":
            MESSAGE = b"l"

        return MESSAGE

    # Will return if snake has collided with opposing snake
    # For now the logic excludes the 2 snake heads
    # This should obviously be changed in the future
    def collision_check(self, MESSAGE, otherSnake):
        for i in range(1, otherSnake.length):
            if self.get_head() == otherSnake.snake[i]:
                MESSAGE = b"c"
                return MESSAGE
        return MESSAGE