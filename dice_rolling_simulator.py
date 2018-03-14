import random
def dice_rolling_simulator():
    random.seed()
    print ('The value is',random.randint(1,6))

def get_yes_no(str_promt):
    answer = input(str_promt + ' ')
    while not ((answer == 'yes') or (answer == 'no')):
        print('This is not a valid answer, please try again.')
        answer = input(str_promt + ' ')
    else:
        if answer == 'yes':
            return True
        else:
            return False

def repeating():
	repeat = True

	while repeat:
			print('Roll the dice!')
			dice_rolling_simulator()
			repeat = get_yes_no('Do you want to roll again? yes/no: ')
repeating()
