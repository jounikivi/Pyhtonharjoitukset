#5.1.14 
# tehtävä
#  9. Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled with yellow, and bars representing values less than 100 are filled with green.

import turtle
xs = [-48, 117, -200, 240, 160, 260, 220]

def draw_bar(t, korkeus):
   
    t.begin_fill()        
    t.left(90)
    t.forward(korkeus)     
    if korkeus >= 0 :
        t.write('  ' + str(korkeus)) 
        t.right(90)
        t.forward(40)         
        t.right(90)
        t.forward(korkeus)     
        t.left(90)            
        t.end_fill()
        t.penup()             
        t.forward(10)         
        t.pendown()
    else:
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(korkeus)
        t.end_fill()
        t.penup()
        t.forward(-(korkeus-15))
        t.right(90)
        t.forward(40)
        t.right(180)
        t.write('  ' + str(korkeus))
        t.forward(40)
        t.right(90)
        t.forward(korkeus-15)
        t.left(90)
        t.forward(10)        
        t.pendown()

wn = turtle.Screen()    
wn.bgcolor("lightgreen") 

piirrä = turtle.Turtle() 
piirrä.pensize(3)         

for v in xs:
    if v >= 200:
        piirrä.color("blue", "red")
    elif 100 <= v < 200:
        piirrä.color("blue", "yellow")
    else:
        piirrä.color("blue", "green")
    draw_bar(piirrä, v)       

wn.exitonclick()