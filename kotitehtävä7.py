#Kohdan 3.8 tehtävä 6
# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)

def draw_regular(name, sides, length):
    for x in range(sides):
        name.forward(length)
        name.left(360 / sides)

import turtle               
wn = turtle.Screen()        
tess = turtle.Turtle()      

draw_regular(tess, 3, 50) 

wn.mainloop()      
