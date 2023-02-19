from board import Board
from ai import AI, RandomAI


#takes in a list of ai's, pairs them up and returns a list of the winners
def run_generation(ai_list: list[AI]) -> list[AI]:
    results = []
    i = 0
    while i < len(ai_list)-1:
        results.add(play_game(ai_list[i], ai_list[i+1]))
    return results

#takes two ai's, plays a game between them, and returns the winner
def play_game(ai1: AI, ai2: AI) -> AI:
    board = Board()


def generate_ai(count: int) -> list[AI]:
    return [RandomAI() for _ in range(count)]
