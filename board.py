class Subboard:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.winner = 0
    

    

class Board:
    def __init__(self):
        self.board = [Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard()]
        self.next_square = -1
        self.next_player = 1