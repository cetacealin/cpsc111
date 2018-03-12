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

