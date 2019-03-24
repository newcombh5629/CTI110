# Create a multi-sided snowflake using the turtle graphics ad range()function.
# 3/23/2019
# CTI-110 P4T1c - Snowflake
# Hoi Newcomb

import turtle                   # allow to use turtles

wn = turtle.Screen()            # create a playground for turtles
wn.title('SnowFlake')           # set the window title
snow = turtle.Turtle()          # create a turtle, assign as snow
snow.color('RoyalBlue')         # set color
snow.pensize(2)                 # set the width of the string
snow.speed(8)                   # set turtle speed

for j in range(12):             # repeat 12 times of a diamond shape
    for i in range(2):          # create a diamond shape
        snow.forward(100)
        snow.right(60)
        snow.forward(100)
        snow.right(120)
    snow.right(30)
    
for j in range(6):              # repeat drawing the 'flakes'
    for i in range(2):          # create the 'flakes'
        snow.forward(240)
        snow.forward(-40)
        snow.left(40)
        snow.forward(25)
        snow.forward(-25)
        snow.right(80)
        snow.forward(40)
        snow.forward(-40)
        snow.left(220)
        snow.forward(200)
    snow.left(30)        

wn.mainloop                     # wait for user to close window




