# write a program display first and last initials using turtle graphics.
# 3/23/2019
# P4T1b - Initials
# Hoi Newcomb

import turtle               # allow us to use turtles
wn = turtle.Screen()        # creates a playground for turtles

b = turtle.Turtle()         # create a turtle, assign to b
b.color('lime green')       # change turtle color
b.shape('turtle')           # assign turtle with different shape
b.speed(1)
b.pensize(5)                # change turtle b pen width

b.penup()                   # raise the pen
b.goto(-150,-150)           # move the turtle start to draw the first initial
b.pendown()                 # put pen down start to draw
b.left(90)                  # turn to the left
b.forward(300)              # move forward 300 units
b.goto(-150,0)              # move the turtle
b.right(90)                 # turn right
b.forward(150)              # move forward 150 units
b.left(90)                  # turn left
b.forward(150)              # move forward 150 units
b.penup()                   # raise the pen
b.goto(0,0)                 # move the turtle
b.pendown()                 # ready to draw
b.forward(-150)             # move backward 150 units
b.penup()                   # raise the pen
                 

b.goto(50,-150)             # move the turtle
b.pendown()                 # ready to draw the last initial
b.forward(300)              # move forward 300 units
b.right(155)                # turn right 155 degree
b.forward(330)              # move forward 330 units
b.right(25)                 # turn right 25 degree
b.forward(-300)             # move upward 300 units

wn.mainloop()               # allow to close the window
