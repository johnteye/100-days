print('Welcome to the tip calculator')

total_bill = float(input('What was the total bill? $'))

people = int(input('How many people to spilt the bill? '))

percentage_tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
#Each person should pay (bill/people) *1.12
tip = percentage_tip/100 * total_bill + total_bill
bill_per_person = tip/ people

#final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
#best way to round to 2 decimal places 
print(f'Each person should pay ${final_amount}')
#f string
print(type(total_bill))
