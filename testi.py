from tkinter import mainloop
import turtle

def  fleur():
  for i in range(300):
    turtle.circle(190-i,90)
    turtle.left(90)
    turtle.circle(190-i,90)
    turtle.left(18)

fleur()
mainloop