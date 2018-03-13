def find_query():
    s = 'labs are "usually" every week'
    strat = s.index('"')
    tail = s[strat+1:]
    print(tail[:tail.index('"')])
find_query()

def find_query2():
    pets = 'cat, dog, mouse, lion'
    start = pets.index(' ')
    tail = pets[start+1:]
    print(tail[:tail.index(',')])
find_query2()
