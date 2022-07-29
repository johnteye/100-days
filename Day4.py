import random

# random_int = random.randint(0, 1)

# if random_int == 1:
# 	print("Heads")
# else:
# 	print("Tails")

# names_string = input("Give me everybody's names, separated by a comma. ")

# names = names_string.split(", ")
# x = len(names)
# random = random.randint(0, x-1)
# print(random)


# print(f"{names[random]} is going to buy the meal today! ") ||harder way

# person_paying = random.choice(names)

# print(f"{person_paying} is going to buy the meal today! ")

row1 = ["◻", "◻", "◻"]
row2 = ["◻", "◻", "◻"]
row3 = ["◻", "◻", "◻"]

map = [row1, row2, row3]
print(map)

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizonal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizonal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
