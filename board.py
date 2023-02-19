class Subboard:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.winner = 0
    
    def get_valid_moves(self):
        return [i for i,j in enumerate(self.board) if j == 0]

    

class Board:
    def __init__(self):
        self.board = [Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard()]
        self.next_square = -1
        self.next_player = 1
    
    def get_valid_moves(self):
        if self.next_square in (0,1,2,3,4,5,6,7,8):
            return [self.next_square * 9 + i for i in self.board[self.next_square].get_valid_moves()]
        else:
            return [i*9 + j for i,b in enumerate(self.board) for j in b.get_valid_moves()]