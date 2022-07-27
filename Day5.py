# Pypassword Generator
import random
'''student_height = input("Input a list of student heights: ").split()
for n in range(0, len(student_height)):
	student_height[n] = int(student_height[n])
print(student_height)


total_height = 0
for height in student_height:
	total_height += height 
print(total_height)


number_of_students = 0
for student in student_height:
	number_of_students += 1
print(number_of_students) '''



# for i in range(1, 101):
# 	if i%3 == 0 and i%5 == 0:
# 		print("FizzBuzz")
# 	elif i  % 3 == 0:
# 		print("Fizz")
# 	elif i % 5 == 0:
# 		print("Buzz")
	
# 	else:
# 		print(i)



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
,'A','B','C', 'D', 'E','F','G', 'H','I', 'J','K','L','M','N','O' ,'P','Q','R','S','T','U','V','W','X','Y','Z']


numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols =['!', '#', '$', '%', '(', ')','*','+']

print("Welcome to the PyPassword Generator")

nr_letters = int(input("How many letters would you like in your password?\n "))

nr_symbols = int(input("How many symbols would you like?\n "))
nr_numbers = int(input("How many numbers would you like?\n "))

password_list = []

for char in range(1, nr_letters + 1):
	password_list.append(random.choice(letters))

for char in range(1, nr_symbols+1):
	password_list.append(random.choice(symbols))

for char in range(1, nr_numbers+1):
	password_list.append(random.choice(numbers))


random.shuffle(password_list)


password = ""

for char in password_list:
	password+=char

print(f"Your password is {password}")
