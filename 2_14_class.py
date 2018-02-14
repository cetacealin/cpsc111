def for_loop():
	for index in range(5):
		#print(index) #print on separate lines
		#print(index, end = ' ') #leave one space
		print(index, end = '\t')
#for_loop()
def traversing_string():
	message = 'Python is fun'
	#print(len(message))
	for index1 in range (len(message)):#left to right
		print(message[index1])
	for index2 in range (-1,-len(message)-1, -1):
		print(index2)

traversing_string()
