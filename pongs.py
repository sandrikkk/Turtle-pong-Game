from turtle import Turtle

coordinates1 = [(350, 0), (350, 20), (350, 40), (350, 60), (350, 80)]
coordinates2 = [(-350, 0), (-350, 20), (-350, 40), (-350, 60), (-350, 80)]


class Pongs:
    def __init__(self):
        self.fragments1 = []
        self.fragments2 = []
        self.create_pong1()
        self.create_pong2()

    def create_pong1(self):
        for segs1 in range(len(coordinates1)):
            segments1 = Turtle()
            segments1.speed("fastest")
            segments1.shape("square")
            segments1.color("green")
            segments1.penup()
            segments1.goto(coordinates1[segs1])
            self.fragments1.append(segments1)

    def create_pong2(self):
        for segs2 in range(len(coordinates1)):
            segments2 = Turtle()
            segments2.speed("fastest")
            segments2.shape("square")
            segments2.color("red")
            segments2.penup()
            segments2.goto(coordinates2[segs2])
            self.fragments2.append(segments2)

    def up1(self):
        for index in range(5):
            new_y = self.fragments1[index].ycor() + 25
            self.fragments1[index].goto(self.fragments1[index].xcor(), new_y)   

    def down1(self):
        for index in range(5):
            new_y = self.fragments1[index].ycor() - 25
            self.fragments1[index].goto(self.fragments1[index].xcor(), new_y)

    def up2(self):
        for index in range(5):
            new_y = self.fragments2[index].ycor() + 25
            self.fragments2[index].goto(self.fragments2[index].xcor(), new_y)

    def down2(self):
        for index in range(5):
            new_y = self.fragments2[index].ycor() - 25
            self.fragments2[index].goto(self.fragments2[index].xcor(), new_y)
