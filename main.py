import web

#web.run()



from ai import RandomAI
import train

ai_list = train.generate_ai(200)
for _ in range(100):
    for _ in range(10):
        ai_list = train.run_generation(ai_list)
    # count the number of random ai's there are
    r = len([1 for ai in ai_list if type(ai) == train.RandomAI])
    # get the average wiin weight of weighted ai's
    w = sum([ai.win_weight for ai in ai_list if type(ai) == train.WeightedAI]) / (len(ai_list) - r)
    # get the average block weight of weighted ai's
    b = sum([ai.block_weight for ai in ai_list if type(ai) == train.WeightedAI]) / (len(ai_list) - r)
    print(f'{r} {w:.2f} {b:.2f}')
    
    winner = next(i for i in ai_list if type(i) == train.WeightedAI)
    randai = RandomAI()
    
    wins = 0
    for i in range(1000):
        wins += int(train.play_game(ai_list[0], randai) == 1)
    print(f'{wins} wins against random ai')
    
    

print(ai_list)
