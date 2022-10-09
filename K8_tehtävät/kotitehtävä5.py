# 5.The two spirals in this picture differ only by the turn angle. Draw both.

def kaksi_kuviota(ttl, trn, fwd):
    
    ttl.color("black")    
    ttl.pensize(3)
    ttl.speed(10)

    ttl.penup()          
    ttl.forward(fwd)

    ttl.pendown()           
    for a in range(0, 100):
        ttl.forward(a * 2)
        ttl.right(trn)

import turtle

wn = turtle.Screen()        
wn.bgcolor("red")
wn.title("kaksi kuviota")

piirä = turtle.Turtle()          
kaksi_kuviota(piirä, 90, -150)

piirä2 = turtle.Turtle()         
kaksi_kuviota(piirä2, 89, 150)    

wn.mainloop()   
