def find_price():
    price= float(input ("enter the price of the item: "))
    sales_tax_rate = float(input('enter the sales tax rate: '))
    sales_tax = price * (sales_tax_rate)
    final_price = price + sales_tax
    print (final_price)

find_price()

def guess_lucky_number(): #the user has to keep entering the number till they get the right number
    lucky_number = 10
    answer = int(input('Guess the lucky number.: '))
    while (answer != lucky_number):
        print('That\'s not the right number! Try again.')
        answer = int(input('Guess the lucky number.: '))
    else:
        print('Bingo!')
guess_lucky_number()
        
def multiple(): #This function is 
    x = int(input('Enter x.: '))
    y = int(input('Enter y.: '))
    z = x * y
    while y != 0:
        a = y
        b = x % y
        x = a
        y = b
    else:
        print ('The least commom multiple of x and y is ',z/x,'.' )
        
multiple()
