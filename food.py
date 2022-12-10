from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.generate_location()
        self.x_random = 0
        self.y_random = 0

    def generate_location(self):
        self.x_random = randint(-280, 280)
        self.y_random = randint(-280, 280)
        self.goto(self.x_random, self.y_random)
