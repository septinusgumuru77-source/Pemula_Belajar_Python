import math 
from turtle import* 

def heart1(k):
    return 15*math.sin(k)**3

def heart2(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
        
speed (0.1)
bgcolor("black")

for i in range(3000):
    for j in range(1):
        color("yellow")
        goto(0.5)
done()