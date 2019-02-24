from turtle import *
from Turtle_exercise_5 import draw_star

speed(0)
color("blue")

for i in range(10):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(30, 100)
    draw_star(x, y, length)