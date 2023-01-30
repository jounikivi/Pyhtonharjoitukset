#5.1.14 
# tehtävä
# 8.Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled with yellow, and bars representing values less than 100 are filled with green.

def draw_bar(t, korkeus):
    if korkeus >= 200:
        t.color("black", "red")
    elif korkeus >= 100:
        t.color("blue", "yellow")
    elif korkeus < 100:
        t.color("white", "darkblue")

    t.begin_fill()             
    t.left(90)                 
    t.forward(korkeus)    

    if korkeus <0:                      
        t.penup()                      
        t.backward(17)                 
        t.write("  "+ str(korkeus))    
        t.forward(17)                 
        t.pendown()                    
    else:                              
        t.write("  "+ str(korkeus))     


    t.right(90)             
    t.forward(40)           
    t.right(90)             
    t.forward(korkeus)      
    t.left(90)             
    t.end_fill()           
    t.penup()              
    t.forward(10)           
    t.pendown()            

import turtle

wn = turtle.Screen()         
wn.bgcolor("lightgreen")

piirrä = turtle.Turtle()      
piirrä.color("blue", "red")
piirrä.pensize(3)

xs = [48,117,200,-240,160,-260,220]     
for a in xs:                          
    draw_bar(piirrä, a)

wn.mainloop()           