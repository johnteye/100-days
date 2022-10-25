# from turtle import Turtle, Screen
# jimmy = Turtle()
# jimmy.shape("arrow")
# print(jimmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Namee",["Pikachu", "Squirtle","Charmader"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)