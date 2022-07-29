# student_scores = {
	
# 	'Harry': 81,
# 	'Ron': 78,
# 	'Hermione':99,
# 	'Draco': 74,
# 	'Neville': 64

# }

# student_grades ={}

# for student in student_scores:
# 	score = student_scores[student]
# 	if score > 90:
# 		student_grades[student] ="Outstanding"
# 	elif score > 80:
# 		student_grades[student] = "Exceeds Expectation"
# 	elif score > 70:
# 		student_grades[student] = "Acceptable"
# 	else:
# 		student_grades[student] = "Fail"



# print(student_grades)


# travel_log =[

# {
# 	"country": "France",
# 	"visits":12,
# 	"cities": ["Paris", "Lillie", "Dijon"]
# },
# {
# 	"country": "Germany",
# 	"visits": 5,
# 	"cities": ["Berlin", "Hambury", "Stuttgart"]
# }
# ]


# def add_new_country(newcountry, new_visits, new_cities):
# 	new_country = {}
# 	new_country["country"] = newcountry
# 	new_country["visits"] = new_visits
# 	new_country["cities"] = new_cities

# 	travel_log.append(new_country)


# add_new_country("Russia", 2, ["Moscow", "Saint Per"])

# print(travel_log)


#### BLIND AUCTION PROGRAM

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
	highest_bid = 0
	winner = ""

	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
	name = input("What is your name? ")
	price = int(input("What's your bid?: $ "))
	bids[name] = price
	should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
	if should_continue == "no":
		bidding_finished = True
		find_highest_bidder(bids)

