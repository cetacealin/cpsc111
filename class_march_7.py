def buildList():
    myList =[]
    element = input('Enter element ')
    while element != '':
	myList.append(element)
	element = input('Enter element ') 
    else:
	print('The list elements: ',myList)
buildList()

