import random
from turtle import Turtle

coordinates = [(-60, 200), ([60, 200])]


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(coordinates[0])
        self.write(self.l_score, align='center', font=("Arial", 60, "normal"))
        self.goto(coordinates[1])
        self.write(self.r_score, align='center', font=("Arial", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.color("red")
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.color("green")
        self.update_scoreboard()

    def l_gamarjveba(self):
        self.goto(0, 0)
        self.color("red")
        self.penup()
        self.hideturtle()
        self.write("წითელმა გაიმარჯვა !", align='center', font=("Arial", 30, "normal"))

    def r_gamarjveba(self):
        self.goto(0, 0)
        self.color("green")
        self.penup()
        self.hideturtle()
        self.write("მწვანემ გაიმარჯვა !", align='center', font=("Arial", 30, "normal"))
