from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 9
        self.y_move = 12

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def change_direction(self):
        self.y_move *= -1

    def change_direction_x(self):
        self.x_move *= -1

    def goal(self):
        self.goto(0, 0)
