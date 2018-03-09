def conditionalExpression():
    num = int(input('Enter an integer: '))
    return ('even' if num%2 == 0 else 'odd')
print (conditionalExpression())

def conditionalExpression_2():
    num = int(input('Enter an integer: '))
    return ( True if num%2 == 0 else False)
print (conditionalExpression_2())

def factorial(num):
    return ( 1 if (num == 1) else num * factorial(num-1))
             
number = int(input('Enter a positive integer: '))
print(factorial(number))

def fact(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * fact(x-1)

for x in range(0,10):
    print('%d! = %d' %(x, fact(x)))

def f(num): #fibonacci sequence
    if (num == 1 or num == 0):
        return 1
    else:
        return f(num-1) + f(num-2)
number = int(input('Enter an integer: '))
print(f(number))

