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
        return "Random_AI"