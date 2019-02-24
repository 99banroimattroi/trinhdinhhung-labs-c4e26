from turtle import *
from Turtle_exercise_3 import draw_square

for i in range(30):
    
    draw_square(i * 5, "red")
    lt(17)
    penup()
    fd(i * 2)
    pendown()

draw_square()