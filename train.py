from board import Board

#takes in a list of ai's, pairs them up and returns a list of the winners
def run_generation(ai_list):
    results = []
    i = 0
    while i < len(ai_list)-1:
        results.add(play_game(ai_list[i], ai_list[i+1]))
    return results

#takes two ai's, plays a game between them, and returns the winner
def play_game(ai1, ai2):
    board = Board()


def generate_ai():
    print ("idk")
