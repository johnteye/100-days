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
            break
        elif user_guess < guess_number:
            print("Too low \nGuess again.")
        else:
            print("Too high. \nGuess again")
        easy_life -= 1
    if easy_life <= 0:
        print(f"Psst the answer is {guess_number}")
def hard():
    hard_life = 5
    while hard_life != 0:
        print(f"You have {hard_life} attempts to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess == guess_number:
            print(f"You got it! The answer was {guess_number} ")
            break
        elif user_guess < guess_number:
            print("Too low \nGuess again.")
        else:
            print("Too high. \nGuess again")
        hard_life -= 1
    if hard_life <= 0:
        print(f"Psst the answer is {guess_number}")
if difficulty == "easy":
    easy()
elif difficulty =="hard":
    hard()
else:
    print("Select an appropriate difficulty")


