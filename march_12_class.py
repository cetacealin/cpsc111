def length(s):#returns: #chars in s
    if s == '':
        return 0

    #s at least one char
    return 1 + length(s[1:])
word = input('enter a word: ') 
print(length(word))

def num_es(s):#returns: #char of "e"'s in s
    if s =='':#s is empty
        return 0
    #s at least one char
    return((1 if s[0] =='e' else 0) + num_es(s[1:]))
word = input('enter a word: ')
print(num_es(word))

def sum_listElements(L1):
    if L1 ==[]:
        return 0
    
    return (L1[0] + sum_listElements(L1[1:]))

#L1 = list(range(4))
#print('\n')
L1 = [5,3,-2,1,9]
print(sum_listElements(L1))

def multiplication_listElements(L1):
    if s =='':
        return 1
    
    return (L1[0] + sum_listElements(L1[1:]))
print(multiplication_listElements(L1))
