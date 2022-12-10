from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("yellow")
        self.speed("fastest")
        self.x_random = randint(-280, 280)
        self.y_random = randint(-280, 280)
        self.goto(self.x_random, self.y_random)
