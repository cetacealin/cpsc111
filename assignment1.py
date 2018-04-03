# Program: cpsc111BV-w18-asg1.py
# Author:Kuan 089988
# Class: CPSC 111BV
# Date: 01/29/2018
# Task: Assignment #1
# Purpose: Solving simple functions learning(), totalProfit(), and getInitials()

def learning(): #This is a function use to ask for user's information and then print the information
    name = input('What is your name?\n')
    program = input('What programming language are you learning?\n')
    print('Today, I found out that',name,'is learning a programming language called',program + '.' + '\n')

learning()

def totalProfit():  #This is a function designed to calculate the toatal profit from selling juice
    juice_cost_price = int(input('Enter the cost price of the juice,\n'))
    juice_sale_price = int(input('Enter the sale price of the juice,\n'))
    cans_sold = int(input('Enter the number of the cans sold,\n'))
    unit_profit = juice_sale_price - juice_cost_price
    total_profit = unit_profit * cans_sold
    print('The toalt profit is',total_profit)

totalProfit()

def getInitials(): #This function will print my initials
    print("""
**	 ***     **
**      ***      **
**    ***        **
**  ***          **
*****            **
**  ***          **
**    ***        **
**      ***      **
**        ***    **********

 """)

getInitials()

#
# Programmer: Kuan Lin
# Date      : Jan. 29, 2018
#
# Program Description: Program to Convert a user entered Celsius temperature into a
#                      corresponding Fahrenheit temperature using the appropriate formula
#

#This function will input the degrees Celsius from the user
def get_degrees_celsius():
    degrees_celsius = int(input('Please, enter your temperature in degrees Celsius(oC):'))
    print('You have entered',degrees_celsius,"oC\n")
    return degrees_celsius
#to_fahrenheit: This function will convert degrees Celsius into degrees Fahrenheit
def to_fahrenheit(cel_temp):
    return (9.0/5.0 * cel_temp + 32)

# main/start program
cel = get_degrees_celsius()
fah = to_fahrenheit(cel)
print ()
print ("The temperature in degrees Fahrenheit, is : ", fah, "oF")
print ()
print ("Thank-you for using the Celsius-Fahrenheit conversion program.")
