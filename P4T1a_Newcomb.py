# write a program that draw both a square and a traingle in turtle graphics, using either a while or for loop.
# 3/22/2019
# CTI-110 P4T1a - Shapes
# Hoi Newcomb


import turtle               # allow us to use turtle
wn = turtle.Screen()        # create a playground for turtle
bob = turtle.Turtle()       # create a turtle, assign to bob
billy = turtle.Turtle()     # create a turtle, assign to billy

for i in range(4):
    bob.forward(100)        # tell turtle to move forward by 100 units
    bob.left(90)            # tell turtle to turn left by 90 degrees

for i in range(3):
    billy.forward(-200)      # tell turtle to move backward by 200 units
    billy.right(120)        # tell turtle to move right by 120 degrees
             
wn.mainloop()               # wait for user to close window
