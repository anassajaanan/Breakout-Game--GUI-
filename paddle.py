from turtle import Turtle

MOVE = 60

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#7F669D")
        self.hideturtle()
        self.shapesize(0.5, 6)
        self.penup()
        self.goto(0, -200)
        self.showturtle()


    def move_right(self):
        if self.xcor() < 210:
            self.setheading(0)
            self.forward(MOVE)


    def move_left(self):
        if self.xcor() > -210:
            self.setheading(180)
            self.forward(MOVE)