from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_update = 10
        self.y_update = 10
    def move(self):
        new_x = self.xcor() + self.x_update
        new_y = self.ycor() + self.y_update
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_update *= -1

    def x_bounce(self):
        self.x_update *= -1

