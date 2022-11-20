from turtle import Turtle
from random import choice

SPEED = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.color("#FF8FB1")
        self.penup()
        self.showturtle()
        x = choice([-1, 1])
        y = choice([-1, 1])
        self.dx = x
        self.dy = y
        self.speed = SPEED

    def move_ball(self):
        self.setx(self.xcor() + (self.dx * self.speed))
        self.sety(self.ycor() + (self.dy * self.speed))
        if self.xcor() > 280:
            self.setx(280)
            self.dx *= -1
        if self.xcor() < -280:
            self.setx(-280)
            self.dx *= -1
        if self.ycor() > 280:
            self.sety(280)
            self.dy *= -1





