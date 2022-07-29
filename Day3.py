# print('Even or Odd Check')
# number = int(input('Enter a number: '))

# if number%2 == 0:
# 	print('Number is Even')
# else:
# 	print('Number is Odd')

# print('Welcome to RollerCoster')

# height = int(input('Enter your height(cm): '))

# if height >= 120:
# 	print('Can ride')
# 	age = int(input('Enter your age: '))
# 	if age < 12:
# 		print('Please pay $5')
# 	elif age <=18:
# 		print('Please pay $7')
# 	else:
# 		print('Please pay $12')

# else:
# 	print('Cannot ride')




#BMI Calculator
# height = float(input('Enter your height in m: '))
# weight = float(input('Enter your weight in kg: '))

# BMI = round(weight/(height **2))
#round to the nearest whole number

# if BMI < 18.5:
# 	print(f'Your BMI is {BMI}, you are underweight')
# elif BMI < 25:
# 	print(f'Your BMI is  {BMI}, you have a normal weight')
# elif BMI < 30:
# 	print(f'Your BMI is  {BMI}, you are overweight')
# elif BMI < 35:
# 	print(f'Your BMI is {BMI}, you are obese')
# else:
# 	print(f'Your BMI is {BMI} you are clinically obese')


#Leap year checker
#hint; divisible but 4 with no remainder is a leap year|if it's evenly divisible by 100 it's still not 
#a leap year| unless it is still evenly divisible by 400 then it's still a leap year

# print('Leap year checker')

# year = int(input('Enter a year: '))

# if year % 4 == 0:
# 	if year%100 == 0:
# 		if year% 400 ==0:
# 			print('Leap year')
# 		else:
# 			print('Not a leap year')

# 	else:
# 		print('Leap')

# else:
# 	print('Not a leap year')

#to count the number of l in love| love.count('l')

print('Welcome to Treasure Island \nYour mission is to find the treasure ')
road = input('You\'re at a cross road.Where do you want to go? Type "left" or "right": ').lower()

if road == "right":
	print('Game over')
else:
	lake = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
	if lake == "Swim":
		print('Game Over')
	else:
		door = input('You arrive at an island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ')
		door =door.lower()
		if door == "red" or door == "Blue":
			print('Game Over')
		else:
			print('You Win')
