lines = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
    (0, 4, 8), (2, 4, 6)             # Diagonals
]



class Subboard:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.winner = 0
        self.valid_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    def make_move(self, move: int, player: int):
        if self.board[move] != 0:
            return False
        
        self.board[move] = player
        self.valid_moves.remove(move)
        
        for a,b,c in lines:
            if self.board[a] == self.board[b] == self.board[c] != 0:
                self.winner = self.board[a]
                self.valid_moves = []
        
        return True

    

class Board:
    def __init__(self):
        self.board = [Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard(), Subboard()]
        self.next_square = -1
        self.next_player = 1
        self.winner = 0
    
    def get_valid_moves(self):
        if self.winner != 0:
            return []
        
        if self.next_square in (0,1,2,3,4,5,6,7,8):
            return [self.next_square * 9 + i for i in self.board[self.next_square].valid_moves]
        else:
            return [i*9 + j for i,b in enumerate(self.board) for j in b.valid_moves]
    
    def make_move(self, move: int) -> bool:
        # make sure it's a valid move
        if not move in self.get_valid_moves():
            return False

        # find the subboard and make the move on it
        square, move = move // 9, move % 9
        self.board[square].make_move(move, self.next_player)
        
        # check if there's a win
        for a,b,c in lines:
            if self.board[a].winner == self.board[b].winner == self.board[c].winner != 0:
                self.winner = self.board[a].winner
        
        self.next_square = -1 if self.board[move].winner != 0 else move
        self.next_player = 3 - self.next_player
        
        return True