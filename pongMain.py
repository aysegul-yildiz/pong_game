from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350, 0))
ball = Ball()
right_score = Score((50,250))
left_score =Score((-50,250))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    elif ball.xcor() > 330 and ball.distance(right_paddle) < 50:
        ball.x_bounce()

    elif ball.xcor() < -330 and ball.distance(left_paddle) < 50:
        ball.x_bounce()

    if ball.xcor() > 350:
        ball.goto(0,0)
        ball.x_bounce()
        left_score.increase()

    elif ball.xcor() < -350:
        ball.goto(0,0)
        ball.x_bounce()
        right_score.increase()

screen.exitonclick()