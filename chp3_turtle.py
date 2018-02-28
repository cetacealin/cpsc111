import turtle
wn = turtle.Screen()
wn.bgcolor("alice blue")
wn.title("Hello, Alex!")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()
alex.color("red")
alex.pensize(5)

tess.left(120) #triangle
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)

tess.right(180) #turn tess around
tess.forward(80) #move her away from the origin

alex.forward(50) #square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()
