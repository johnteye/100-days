'''import math

def paint_calc(height, width, cover):
	num_of_cans = math.ceil((height * width)/cover)
	#rounding up to the nearest whole number
	print(f"You'll need {num_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover = coverage)'''

print(''' 

  ,ad8888ba,                                                                                                 88                                 
 d8"'    `"8b                                                                                                88                                 
d8'                                                                                                          88                                 
88            ,adPPYYba,  ,adPPYba, ,adPPYba,  ,adPPYba, 8b,dPPYba,        ,adPPYba, 8b       d8 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88            ""     `Y8 a8P_____88 I8[    "" a8P_____88 88P'   "Y8       a8"     "" `8b     d8' 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
Y8,           ,adPPPPP88 8PP"""""""  `"Y8ba,  8PP""""""" 88               8b          `8b   d8'  88       d8 88       88 8PP""""""" 88          
 Y8a.    .a8P 88,    ,88 "8b,   ,aa aa    ]8I "8b,   ,aa 88               "8a,   ,aa   `8b,d8'   88b,   ,a8" 88       88 "8b,   ,aa 88          
  `"Y8888Y"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"'  `"Ybbd8"' 88                `"Ybbd8"'     Y88'    88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                         d8'     88                                             
                                                                                        d8'      88          


	''')



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
  




should_end = False
while not should_end:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")



