import random
def dice_rolling_simulator():
	for i in range (1):
		print ('The value is',random.randint(1,6))

def get_yes_no(str_promt):
	answer = input(str_promt + ' ')
	while answer == 'yes':
		return True
	else:
		if answer == 'no':
			return False
		
		else:
			print('this is not a valid answer, please try again.')
			answer = input(str_promt + ' ')
			return True
def repeating():
	first_time = True
	repeat = True

	while repeat:
		if first_time:
			print('Roll the dice!')
		else:
			print('Roll the dice!')
		dice_rolling_simulator()
		repeat = get_yes_no('DO you want to roll again?')
		first_time = False
repeating()
