def warm_up():
    course = "Introduction to Computing"
    Credits = 4
    Characters = 18
    pi = 3.141592653589793
    print ("course is " + course)
    print ("Credits", Credits)
    print ("Characters", Characters)
    print ("pi", pi)
    print ("\n")

warm_up()

def example_1():
    print ("hello\n")
    print ("To print a newline use \\n")
    print ("She said: \"hello\"")
    print ("\tThis is indented")
    print ("This is a very, very, very, very, very, very \
long print statment")
    print ("""
This is a multi-line print statement
First line
Second line
""")
    print("\n")
    # I can also use triple single quotations ‘’’ ‘’’

example_1()

def exercise_1():
    print ("\  |  /")
    print ("  @ @")
    print ("   *")
    print (' \\"""/')
    print ("\n")

exercise_1()

def example_2(): #String operations
    b = "the"
    c = "cat"
    d = " is on the mat"
    a = b + " " + c + d
    print (a)
    b = b + " "
    a = b * 5
    print (a)
    print ("The first character of", c, "is" ,c[0])
    print ("The word \""+ c+ "\" has", len(c) ,"characters")
    name = input("Please, type in your name ")
    name = (name + "!") * 5
    print (name)
    print("\n")

example_2()

def exercise_2():
    answer = input("What is your favorite color?")
    a = answer
    color_length = len(a)
    empty_string = " " * color_length + " "
    b = " "
    c = answer + b
    print (c * 9 + a)
    print (c + (empty_string * 8) + a)
    print (c + (empty_string * 8) + a)
    print (c * 9 + a)
    print("\n")

exercise_2()

def getYourOpinion():
    answer = input("Do you like Python? ")
    if answer == "yes":
       print ("That is great!")
    else:
       print ("That is disappointing!")
    print("\n")

getYourOpinion()

def exercise_3():
    answer = input ("Do you wanna build a snowman?")
    if answer == "yes":
        print ("That is great!")
    elif answer == "no":
        print ("That is disppointing!")
    else:
        print ("That is not an answer to my question.")
        print("\n")

exercise_3()

#--------------------------------------------------------------------------
# convert.py
# Created by: A. Malki
# A program for converting a weight from pounds to kilograms
#--------------------------------------------------------------------------

def pounds_kilos_conversion():
    pounds = int(input("Enter a weight in pounds (lbs.): "))
    kilos = 0.45359237 * pounds
    print ("The weight in kilograms is", kilos)
    print("\n")

pounds_kilos_conversion()

#--------------------------------------------------------------------------
# convert.py
# Created by: Kuan Lin
# A program for converting a temperature from Fahrenheit to Celsius
#--------------------------------------------------------------------------

def Fahrenheit_Celsius_conversion():
    Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
    Celsius = (Fahrenheit - 32.0) * 5.0 / 9.0
    print("The temperature in Celsius is", Celsius)
    print("\n")

Fahrenheit_Celsius_conversion()

