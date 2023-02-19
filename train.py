from board import Board
from ai import AI, RandomAI, InvalidRandomAI
import random


#takes in a list of ai's, pairs them up and returns a list of the winners
def run_generation(ai_list: list[AI]) -> list[AI]:
    for i in range(0, len(ai_list), 2):
        winner = play_game(ai_list[i], ai_list[i + 1])
        if winner == 1:
            ai_list[i + 1] = ai_list[i].clone()
        else:
            ai_list[i] = ai_list[i + 1].clone()
    random.shuffle(ai_list)
    return ai_list

#takes two ai's, plays a game between them, and returns the winner
def play_game(ai1: AI, ai2: AI) -> AI:
    board = Board()
    while True:
        if not board.make_move((ai1, ai2)[board.next_player - 1].play(board)):
            return (ai1, ai2)[2 - board.next_player]

#generates list of N ai's
def generate_ai(count: int) -> list[AI]:
    return [InvalidRandomAI(.5) for _ in range(count)]
