from abc import ABC, abstractmethod

from board import Board

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
    
    def __str__(self):
        return 'RandomAI'


# AI which has a chance of making an invalid move
class InvalidRandomAI(RandomAI):
    def __init__(self, invalid_chance: float):
        self.invalid_chance = invalid_chance
    
    def play(self, board: Board) -> int:
        move = super().play(board)
        if random.random() < self.invalid_chance:
            return -1
        return move
    
    def clone(self):
        r = random.random()
        r = r * .01 + self.invalid_chance * .99
        return InvalidRandomAI(r)
    
    def __str__(self):
        return f'InvalidRandomAI ({self.invalid_chance:%.2f})'
