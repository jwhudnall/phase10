#future addition: convert winners to list of dictionaries with name:points if player has reached phase 10

winners = []
players = []
while True:
	try:
		player_count = int(input("Number of players: "))
	except ValueError:
		print("Please enter a number. ")
	else:
		break

#Populates the players list
for num in range(1,player_count+1): 
	name = input(f"Who is player {num}? ")
	new_player = [name.title(),{'phase':1},{'points':0}]
	players.append(new_player)

#TEST ONLY ex: jim is on phase 0 and has 0 points.
# for player in players:
# 	print(f"{player[0]} is on phase {player[1]['phase']} and has {player[2]['points']} points.")

#Hand starts
#Validates round winner


while len(winners) == 0:
	# for player in players:
	# 	if player[1]['phase'] == 'Complete':
			

	print(f"New round!")
	while True:
		round_winner = input("Who won the round? ")
		if round_winner.title() not in [player[0] for player in players]:
			print("Please enter a valid player name.")
		else: 
			#print(f"Good Job. {round_winner} is a valid player")
			break

	#establishes who won. Player will receive 0 points but progress 1 phase	
	for player in players:
		if round_winner.title() == player[0]:
			if player[1]['phase'] < 10:
				player[1]['phase'] += 1
			else:
				#Player has finished Phase 10 and has their name and points added as a dictionary to "winners" list
				player[1]['phase'] = 'Complete'
				winners.append([player[0],[player[2]]])
		else:
			while True:
				phase_increase = input(f"Did {player[0]} make their phase? ")
				if phase_increase[0].lower() == 'y':
					#new logic try
					if player[1]['phase'] < 10:
						player[1]['phase'] += 1
						break
					else:
						player[1]['phase'] = 'Complete'
						winners.append([player[0],[player[2]]])
						break
				elif phase_increase[0].lower() == 'n':
					break
				else:
					print("Please type yes or no. ")
					
					
			while True: #ensures an integer is given
				try:
					point_accrual = int(input(f"How many points did {player[0]} have? "))
				except ValueError:
					print("Please enter a number. ")
				else:
					break
			player[2]['points'] += point_accrual
	print("At the end of the round:")
	print("="*50)
	for player in players:
		print(f"{player[0]} is on phase {player[1]['phase']} and has {player[2]['points']} points.")
	print("="*50)
	##break loop when 'complete'

#Need to add logic to discern winner if > 1
print("The gamer is over!")
if len(winners) == 1:
	print(f"{winners[0][0]} has won the game! ")
else:
	print(winners)









#round1 - player goes out
# while hand <=10:
# 	print(f"We're on round {hand}.\n{hand}'s and Jokers are wild.\nDeal those cards!")
# 	print("*" * 30)
# 	while True:
# 		knocker = input(f"For round {hand}, who knocked? ")
# 		if knocker.title() not in players:
# 			print("Please enter a valid player name.")
# 		else:
# 			break

# for player in players:

