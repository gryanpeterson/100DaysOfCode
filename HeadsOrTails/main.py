import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

coin_toss = random.randint(0,1)

if coin_toss == 1:
    print("Heads")
else:
    print("Tails")

