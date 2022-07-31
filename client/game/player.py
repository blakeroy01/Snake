class Player:
    def __init__(self, length, id, snake):
        self.length = length
        self.id = id
        self.snake = snake
    
    def update_player(self, length, head):
        self.length = length
        self.snake = head


def create_new_player(length, id, snake):
        return Player(length, id, snake)

        
    