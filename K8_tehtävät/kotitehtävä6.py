# 10.Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like this:

def piirä_tähti(ttl):
    

    ttl.pendown()           
    for x in range(5):      
        ttl.forward(100)
        ttl.right(144)
    
    ttl.penup()             

import turtle

wn = turtle.Screen()        
wn.bgcolor("lightgreen")    

piirä = turtle.Turtle()      
piirä.color("whitesmoke")       
piirä.pensize(3)
piirä.penup()                

piirä.backward(175)         
piirä.left(90)
piirä.forward(60)
piirä.right(90)

for dummy in range(5):      
    piirä_tähti(piirä)    
    piirä.forward(350)       
    piirä.right(144)         

wn.mainloop()   