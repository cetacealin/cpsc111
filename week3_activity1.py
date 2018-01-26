def substract(num1, numb2):
    difference = num1 - num2
    return difference

num1 = int(input('Give me a number'))
num2 = int(input('Give e another number'))
print(substract(num1, num2), '\n')

def substract_easy_way(num1, num2):
    return num1 - num2

num1 = int(input('Give me a number'))
num2 = int(input('Give me another number'))
print(substract_easy_way(num1, num2), '\n')

def enter_your_name():
    name = input('Enter your name ')
    print('Hello, my name is ' + name + '\n' + name + ' is in this class' + '\n' + 'Without a doubt ' + name + ' is working on this task' +  '\n')

enter_your_name()

def getName():
    Name = input('What is your name? ')
    return Name

def greet():
    print("Welcome",getName())

greet() 
