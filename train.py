from board import Board
from ai import AI, RandomAI, InvalidRandomAI, WeightedAI
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
def play_game(ai1: AI, ai2: AI) -> int:
    board = Board()
    while True:
        move = (ai1, ai2)[board.next_player - 1].play(board)
        if not board.make_move(move):
            return board.winner or 3 - board.next_player

#generates list of N ai's
def generate_ai(count: int) -> list[AI]:
    return [RandomAI() for _ in range(count // 2)] + [WeightedAI(5510, 2840) for _ in range(count // 2)]
