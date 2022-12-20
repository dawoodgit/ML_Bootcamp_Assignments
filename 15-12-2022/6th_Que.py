#You have to develop a number guessing game.

import random
num = random.randint(1,101)
while True:
    a = int(input("Guess:"))

    if a <= 0:
        print("Thanks for playimg the game! The correct number was:",num)
        break
    
    elif a == num:
        print("Congratulations! You guessed it right.")
        break

    elif a > num:
        print("Number too large")
    
    else:
        print("Number too small.")