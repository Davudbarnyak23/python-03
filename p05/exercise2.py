#game
import random
print("\u2591" * 40)
print("\u2591"*4, "duflfq xbckj dsl 0 lj 3","\u2591"*4)
print("\u2591" * 40)

n = 0

for i in range(1, 5 ):
    print(f"raund:  {i}:", end="")

    random_number = random.randint(1,3)
    number = int(input(" input number:" ))
    if random_number == number:
        print("you win!")
        n += 1
    else:
        print("you noy win!")

print('N= ', n)