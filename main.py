import web

web.run()



import train
ai_list = train.generate_ai(1000)
for _ in range(10):
    for _ in range(100):
        ai_list = train.run_generation(ai_list)
    print(sum(a.invalid_chance for a in ai_list) / len(ai_list))

print(ai_list)