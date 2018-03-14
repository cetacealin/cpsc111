#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program: cpsc111BV-w18-asg3.py
# Author: Kuan Lin ID: 089988, Chang Suk Lee(Jason) ID: 090006, 
# Class: CPSC 111BV
# Date: 03/01/2018
# Task: Assignment #3
# Purpose: working with functions, for loops, Numbers & turtles           
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# pyramid()
# Parameters: none 
# Return Value: none
# Description:
#   This function will asks the user for an integer which is the number of lines printed.
#   Then, the function will use an algorithm to print pyramid shape made up of numbers.
#   The middle number on the line is 2 ** (k - 1) and the biggest number in the line.
#   From left to middle number, number is increasing 2 ** (k - 1),
#   From middle number to right, number is decreasing 2 ** (k - 1), 

def pyramid():
    
    n = int(input("Type the number of rows for the pyramid: ")) # Get an integer from the user
    spacing = len(str(2 ** (n - 1) )) # Get the length of the largest possible number to figure out suitable spacing
    num_spaces = ((spacing+1) * (n-1)) # Number of spacing needed to reach the middle point of the last row


    for i in range(1, n+1): # For loop for the rows

        for j in range(0, num_spaces): # Print " " until it reach the point where it should start printing the numbers
            print(end=" ")

        num_spaces -=  spacing + 1 # Reducing num_spaces  for the next row in order to make pyramid shape

        for k in range(1, i+1): # For loop(Left to Right) increasing order of 2 ** k - 1
            adj_spacing = spacing - len(str(2 ** k )) + 1  # Calculate the length of the next number and adjust the spacing
            if k == i :
                last_spacing = spacing - len(str(2 ** (k-2) )) + 1 # Spacing after middle number
                print(str(2**(k-1)) + (" " * last_spacing), end = "") # Print 2 ** (k-1) and spaces
            else:   
                print(str(2**(k-1)) + (" " * adj_spacing), end = "") # Print 2 ** (k-1) and spaces

        for l in range(i-1,0,-1): # For loop(Right to Left) decreasing order of 2 ** k - 1
            adj_spacing = spacing - len(str(2 ** (l-2))) + 1 # Calculate the length of the next number and adjust the spacing
            print(str(2**(l-1)) + (" " * adj_spacing), end = "")# Print 2 ** (k-1) and spaces

        print("\r") # End the row and move on to the next row.

        
pyramid()

# Part 2

# Question 1

import turtle # Import Turtle Module

wn  = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Assignment 3 - Part 2")

nemo = turtle.Turtle()
nemo.color("hotpink")
nemo.pensize(5)
nemo.penup()
nemo.left(90) # Adjusting initial position
nemo.forward(250)
nemo.left(90)
nemo.forward(250)
nemo.pendown()
for i in range(6): # Hexagon Using For Loop
    nemo.left(60)
    nemo.forward(50)

dory = turtle.Turtle()
dory.color("orange")
dory.pensize(5)
dory.left(180) # Adjusting initial position
dory.penup()
dory.forward(150)
dory.right(90)
dory.forward(200)
dory.left(90)
dory.pendown()
for i in range(3): # Equilateral Triangle Using For Loop
    dory.right(120)
    dory.forward(50)

# Question 2

haze = turtle.Turtle() 
haze.penup()
haze.left(180) # Adjusting initial position of turtle
haze.forward(100)
haze.right(180)
haze.pendown()
haze.color("blue")
haze.pensize(5)
haze.shape("turtle")

for i in range(12): #Drawing clock Using For Loop
    haze.penup()
    haze.forward(60)
    haze.pendown()
    haze.forward(30)
    haze.penup()
    haze.forward(30)
    haze.stamp()
    haze.left(180)
    haze.forward(120)
    haze.left(180)
    haze.right(30)

# Question 3

isu = turtle.Turtle()
isu.fillcolor("yellow")
isu.pensize(5) # Adjusting initial position
isu.penup()
isu.forward(200)
isu.pendown()

isu.begin_fill() # Drawing house
isu.left(90)
isu.forward(100) # 1 stroke
isu.left(50)
isu.forward(66) # 2 stroke
isu.left(80)
isu.forward(66) # 3 stroke
isu.end_fill() # Fill 1/2
isu.begin_fill()
isu.left(95)
isu.forward(142) # 4 stroke
isu.right(135)
isu.forward(100) # 5 stroke
isu.right(90)
isu.forward(100) # 6 stroke
isu.end_fill() # Fill 2/2
isu.right(90)
isu.forward(100) # 7 stroke
isu.right(135)
isu.forward(142) # 8 stroke

wn.mainloop()

