import random
from turtle import Turtle

colors = ["red", "yellow", "purple", "white"]

class Dashed_line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(3)
        self.penup()
        self.goto(0, -340)
        self.dashed_line1()

    def dashed_line1(self):
        self.setheading(90)
        for index in range(12):
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()
            self.color(random.choice(colors))

