import sys

print('Let\'s fix the previous code with exception handling')

try:
    number = int(input('Enter a number between 1-10'))
except ValueError:
    print('Err...numbers only')
print('you entered number',number)
