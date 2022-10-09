# 5.The two spirals in this picture differ only by the turn angle. Draw both.

def kaksi_kuviota(ttl, trn, fwd):
    
    ttl.color("black")    
    ttl.pensize(1.5)
    ttl.speed(10)

    ttl.penup()          
    ttl.forward(fwd)

    ttl.pendown()           
    for a in range(0, 100):
        ttl.forward(a * 2)
        ttl.right(trn)

import turtle

wn = turtle.Screen()        
wn.bgcolor("lightgreen")
wn.title("kaksi kuviota")

piirä = turtle.Turtle()          
kaksi_kuviota(piirä, 90, -150)   

alex = turtle.Turtle()         
kaksi_kuviota(piirä, 89, 150)    

wn.mainloop()   
