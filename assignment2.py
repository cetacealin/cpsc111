#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program: cpsc111BV-w18-asg2.py
# Author: Chang Suk Lee(Jason) ID: 090006, Kuan Lin ID: 089988
# Class: CPSC 111BV
# Date: 02/13/2018
# Task: Assignment #2
# Purpose: Making a simple calculator program
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# getInteger()
# Parameters:
#   str_prompt - A String which will be shown to the users to "prompt" them.
# Return Value:
#   An integer.
# Description:
#   This function will accept one string as a parameter and print it.
#   Then, the function get input from the user and convert it into an integer.
#   If the user does not enter a proper integer, print an error message, print the prompt message, and get input from the user again.
#   Return an integer when the given input can be successfully converted to an integer.

def getInteger(str_prompt) :
    
    given_int = input(str_prompt + " ") # This variable stores an input from users

    while (not given_int.isdigit()): # Check whether given input can be converted to an integer
        print("Not a valid number, try again...\n") 
        given_int = input(str_prompt + " ")
    else :
        return int(given_int)
    
    
# getMathOp()
# Parameters:
#   str_prompt - A String which will be shown to the users to "prompt" them.
# Return Value:
#   A string with one of four values: "+", "-", "*", "/", or "**"
# Description:
#   This function will accept one string as a parameter and print it.
#   Then, the function get input from the user and check whether given input is a single sign out of the set **,+,-,*,/
#   If the user does not enter a proper math op, print an error message, print the prompt message, and get input from the user again.
#   Return a astring when the given input is a single sign out of the set **,+,-,*,/

def getMathOp(str_prompt):
    
    given_Op = input(str_prompt + " ") # This variable stores an input from users

    # Check whether given input is one of four values:  "+", "-", "*", "/", or "**"
    while not ((given_Op == "+") or (given_Op == "-") or (given_Op == "/") or (given_Op == "*") or (given_Op == "**")) :
        print("You may only enter one of the characters: ** + - * /\n")
        given_Op = input(str_prompt + " ")
    else :
        return given_Op


# getYesNo()
# Parameters:
#   str_prompt - A String which will be shown to the users to "prompt" them.
# Return Value:
#   Boolean - True if the user entered yes, False if the user entered no
# Description:
#   This function will accept one string as a parameter and print it.
#   Then, the function get input from the user and check it whether it's either 'yes' or 'no'.
#   If the user does not enter a proper input print an error message, print the prompt message, and get input from the user again.
#   Return True if given input is 'yes', and return False if given input is 'no'

def getYesNo(str_prompt):
    
    given_bool = input(str_prompt + " ") # This variable stores an input from users

    # Check whether given input is either 'yes', or 'no'
    while not ((given_bool == "Yes") or (given_bool == "yes") or (given_bool == "No") or (given_bool == "no") ) :
        print("Not a valid answer, enter yes or no.\n")
        given_bool = input(str_prompt + " ")
    else:
        if ((given_bool == "Yes") or (given_bool == "yes") ):
            return True
        else:
            return False


# doCalculation()
# Parameters:
#   none
# Return Value:
#   Float - Result of calculation.
# Description:
#   This function will call getInteger(), getMathOp(), and getInter() one after the other.
#   Then, the function perform the appropriate calculation, print and return the result in a float.

def doCalculation():

    int1 = getInteger("Enter your first number:") # Get the first integer from user
    op = getMathOp("Enter your math operation:") # Get the math operator from user
    int2 = getInteger("Enter your second number:") # Get the second integer from user

    if op == "+":  # Print and return int1 + int2
        print()
        print("Result:", int1, "+", int2, "=", float(int1 + int2), "\n")
        return float(int1 + int2)
    elif op == "-": # Print and return int1 - int2
        print()
        print("Result:",int1, "-", int2, "=", float(int1 - int2), "\n")
        return float(int1 - int2)
    elif op == "*": # Print and return int1 * int2
        print()
        print("Result:",int1, "*", int2, "=",  float(int1 * int2), "\n")
        return float(int1 * int2)
    elif op == "/": # Print and return int1 / int2
        print()
        print("Result:",int1, "/", int2, "=",  float(int1 / int2), "\n")
        return float(int1 / int2)
    else : # Print and return int1 ** int2
        print()
        print("Result:",int1, "**", int2, "=",  float(int1 ** int2), "\n")
        return float(int1 ** int2)
    

# calculator()
# Parameters:
#   none
# Return Value:
#   none
# Description:
#   This function print "Perfrom the first calculation" if it's the first calculation. Otherwise, print "Perform the next calculation"
#   Then the functino will ask the user 2 integers and one math op.
#   Next, the function will perform the appropriate calculation, print and return the result in a float.
#   This function will ask the users if they want to do another calculation, after each calculation.
#   If the users say 'yes', do another calculation. Otherwise, print "Goodbye!" and terminate the program.

def calculator():
    
    first_time = True # This variable is True when the program is perfroming first calculation. False otherwise.
    repeat = True # This variable is True when the user want to do another calculation. False otherwise.

    while repeat: # Check whether user want to repeat or not.
        
        if first_time: # Check whether it's first calculation or not
            print("Perform the first calculation\n")
        else:
            print()
            print("Perform the next calculation\n")

        doCalculation() # Call do Calculation()
        repeat = getYesNo("Would you like to perform another calculation? (yes or no)")
        first_time = False

    else: # Print "Goodbye!" if user don't want another calculation
        print("Goodbye!")

calculator()
            

    
    

    


    
