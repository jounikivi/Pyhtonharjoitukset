#Kohdan 3.8 tehtävä 11
#Write a program to draw a shape like this:

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

# Customize speed and pen thickness.
tess.speed(3)
tess.pensize(3)

# Draw the actual shape
for x in range(5):
    tess.forward(200)
    tess.right(144)

# Make the turtle hide so just the shape displays.
tess.hideturtle()

# Hold the window open till the user closes it.
wn.mainloop()