import random
def dice_rolling_simulator():
		print ('The value is',random.randint(1,6))

def get_yes_no(str_promt):
	answer = input(str_promt + ' ')
	if answer == 'yes':
		return True
	else:
		if answer == 'no':
			return False
		
		else:
			print('this is not a valid answer, please try again.')
			answer = input(str_promt + ' ')
			return True
def repeating():
	repeat = True

	while repeat:
			print('Roll the dice!')
			dice_rolling_simulator()
			repeat = get_yes_no('DO you want to roll again? yes/no: ')
repeating()
