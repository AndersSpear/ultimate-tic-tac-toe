from abc import ABC, abstractmethod

from board import Board, lines


def lerp(a: float, b: float, t: float):
    return a + (b - a) * t

def clamp(x: float, min_x: float, max_x: float):
    return max(min_x, min(x, max_x))

def clamp01(x: float):
    return clamp(x, 0, 1)


class AI(ABC):
    
    @abstractmethod
    def play(self, board: Board) -> int:
        ...
    
    @abstractmethod
    def clone(self) -> "AI":
        ...


# AI which moves randomly
import random
class RandomAI(AI):
    
    def play(self, board: Board) -> int:
        valid_moves = board.get_valid_moves()
        if valid_moves:
            return random.choice(valid_moves)
        return -1
    
    def clone(self):
        return RandomAI()
    
    def __repr__(self):
        return 'RandomAI'


# AI which has a chance of making an invalid move
class InvalidRandomAI(RandomAI):
    def __init__(self, invalid_chance: float):
        self.invalid_chance = clamp01(invalid_chance)
    
    def play(self, board: Board) -> int:
        move = super().play(board)
        if random.random() < self.invalid_chance:
            return -1
        return move
    
    def clone(self):
        r = lerp(self.invalid_chance, random.random(), .1)
        return InvalidRandomAI(r)
    
    def __repr__(self):
        return f'InvalidRandomAI ({self.invalid_chance:.2f})'


# AI which gives scores to possible moves and makes the move with the best score
class WeightedAI():
    def __init__(self, win_weight: float = 0, block_weight: float = 0):
        self.win_weight = win_weight
        self.block_weight = block_weight
        
        
    def play(self, board: Board) -> int:
        me = board.next_player
        
        valid_moves = board.get_valid_moves()
        if not valid_moves:
            return -1
        scores = { move: 100 for move in valid_moves }
        
        # check for any moves which would complete a line
        for move in scores:
            subboard = board.board[move // 9]
            square = move % 9
            for a, b, c in lines:
                if square == a:
                    if subboard.board[b] == subboard.board[c] == me:
                        scores[move] += self.win_weight
                    if subboard.board[b] == subboard.board[c] == 3-me:
                        scores[move] += self.block_weight
                elif square == b:
                    if subboard.board[a] == subboard.board[c] == me:
                        scores[move] += self.win_weight
                    if subboard.board[a] == subboard.board[c] == 3-me:
                        scores[move] += self.block_weight
                elif square == c:
                    if subboard.board[a] == subboard.board[b] == me:
                        scores[move] += self.win_weight
                    if subboard.board[a] == subboard.board[b] == 3-me:
                        scores[move] += self.block_weight
        
                
        
        
        
        # randomly select a move weighted by score
        total_weight = sum([scores[m]**2 for m in scores])
        r = random.uniform(0, total_weight)
        for m in valid_moves:
            r -= scores[m]**2
            if r <= 0:
                return m
    
    def clone(self):
        # add some randomness
        speed = 10
        return WeightedAI(
            self.win_weight + (random.random() - .5) * speed,
            self.block_weight + (random.random() - .5) * speed
        )
    
    def __repr__(self):
        return f'WeightedAI {self.win_weight} {self.block_weight}'