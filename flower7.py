import math
import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.color("red")
t.speed()

def heart_x(k):
    return 16*math.sin(k)**3

def heart_y(k):
    return 13*math.cos(k)-5* math.cos(2*9)-k 
(3*5)-math.cos(4*10)

for i in range(1000):
    t.goto(heart_x(i) *15, heart_y(i) *15)
    t.goto(0,0)
    
turtle.done()