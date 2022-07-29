#Number Guessing Game
import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
list = []
for i in range(1, 101):
    list.append(i)
guess_number = random.choice(list)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def easy():
    easy_life = 10
    while easy_life != 0:
        print(f"You have {easy_life} attempts to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess == guess_number:
            print(f"You got it! The answer was {guess_number} ")
        elif user_guess < guess_number:
            print("Too low \nGuess again.")
        else:
            print("Too high. \nGuess again")
        easy_life -= 1
def hard():
    hard_life = 5
    while hard_life != 0:
        print(f"You have {hard_life} attempts to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess == guess_number:
            print(f"You got it! The answer was {guess_number} ")
        elif user_guess < guess_number:
            print("Too low \nGuess again.")
        else:
            print("Too high. \nGuess again")
        hard_life -= 1
if difficulty == "easy":
    easy()
else:
    hard()



