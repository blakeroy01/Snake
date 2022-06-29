class Player:
    def __init__(self, length, id, snake):
        self.length = length
        self.id = id
        self.snake = snake

    
def create_new_player(length, id, snake):
        return Player(length, id, snake)
        
    