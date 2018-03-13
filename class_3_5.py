def listTraversalUsingWhileLoop():
    friends = ["Oscar","Ryan","Jess","Jessica","Eunice"]
    index = 0
    while (index < len(friends)):
        print(friends[index], end = " ")
        index +=1


def listTraversalUsingForLoop():
    friends = ['Oscar','Ryan','Jess','Jessica','Eunice']
    for i in range (len(friends)):
        print(friends[i], end = " ")

listTraversalUsingWhileLoop()
print('\n')
listTraversalUsingForLoop()

