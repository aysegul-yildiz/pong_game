from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.count = 0
        self.display_score(position)
        self.position = position


    def display_score(self,position):
        self.goto(position)
        self.clear()
        self.write(self.count ,align = "center", font = ("calibri", 40,"bold") )

    def increase(self):
        self.count += 1
        self.display_score(self.position)

