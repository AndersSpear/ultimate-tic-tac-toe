from abc import ABC, abstractmethod

from board import Main_board

class AI(ABC):
    
    @abstractmethod
    def play(self, board: Main_board) -> int:
        ...
    
    @abstractmethod
    def clone(self) -> "AI":
        ...


# AI which moves randomly
import random
class RandomAI(AI):
    
    def play(self, board: Main_board) -> int:
        valid_moves = board.get_valid_moves()
        if valid_moves:
            return random.choice(valid_moves)
        return -1
    
    def clone(self):
        return RandomAI()
    
    def __str__(self):
        return "Random_AI"