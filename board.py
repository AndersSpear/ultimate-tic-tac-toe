class Sub_board:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.winner = 0
    

    

class Main_board:
    def __init__(self):
        self.board = [Sub_board(), Sub_board(), Sub_board(), Sub_board(), Sub_board(), Sub_board(), Sub_board(), Sub_board(), Sub_board()]
        self.next_square = -1
        self.next_player = 1