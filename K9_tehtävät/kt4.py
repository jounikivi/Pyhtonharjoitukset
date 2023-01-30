#5.1.14 
# tehtävä
# 7. Modify the turtle bar chart program so that the pen is up for the small gaps between each bar.

def draw_bar(t, korkeus):
    t.begin_fill()           
    t.left(90)
    t.forward(korkeus)
    t.write("  "+ str(korkeus))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(korkeus)
    t.left(90)
    t.end_fill()             
    t.forward(10)
    
import turtle

wn = turtle.Screen()        
wn.bgcolor("blue")

piirrä = turtle.Turtle()       
piirrä.color("black", "red")
piirrä.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(piirrä, a)
    
wn.mainloop()