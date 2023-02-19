from abc import ABC, abstractmethod

from board import Main_board

class AI(ABC):
    
    @abstractmethod
    def play(self, board: Main_board) -> int:
        ...
    
    @abstractmethod
    def clone(self) -> "AI":
        ...
