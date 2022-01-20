from turtle import Screen
from pongs import Pongs
from ball import Ball
from dashed_line import Dashed_line
from score import Score
import time
screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("სანდროს Pong")
screen.tracer(0)

pong = Pongs()
dashed_line = Dashed_line()
score = Score()

screen.update()

screen.onkey(pong.up1, "Up")
screen.onkey(pong.down1, "Down")

screen.onkey(pong.up2, "w")
screen.onkey(pong.down2, "s")

screen.listen()
is_game_on = True
ball = Ball()
while is_game_on:
    ball.move()
    time.sleep(0.0099)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction()

    for index in pong.fragments1:
        if ball.distance(index) < 30 and ball.xcor() > 340:
            ball.change_direction_x()

    for index in pong.fragments2:
        if ball.distance(index) < 30 and ball.xcor() < 340:
            ball.change_direction_x()

    if ball.xcor() > 380:
        score.l_point()
        ball.goal()

    if ball.xcor() < -380:
        score.r_point()
        ball.goal()
    if score.l_score == 3 or score.r_score == 3:
        if score.l_score > score.r_score:
            score.l_gamarjveba()
            is_game_on = False
        else:
            score.r_gamarjveba()
            is_game_on = False

screen.exitonclick()
