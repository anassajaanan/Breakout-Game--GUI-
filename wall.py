from turtle import Turtle

LIST_POSITIONS1 = [(-240, 240), (-180, 240), (-120, 240), (-60, 240), (0, 240), (60, 240), (120, 240), (180, 240), (240, 240)]
LIST_POSITIONS2 = [(-240, 210), (-180, 210), (-120, 210), (-60, 210), (0, 210), (60, 210), (120, 210), (180, 210), (240, 210)]
LIST_POSITIONS3 = [(-240, 180), (-180, 180), (-120, 180), (-60, 180), (0, 180), (60, 180), (120, 180), (180, 180), (240, 180)]
LIST_POSITIONS4 = [(-240, 150), (-180, 150), (-120, 150), (-60, 150), (0, 150), (60, 150), (120, 150), (180, 150), (240, 150)]


class Wall:

    def __init__(self):
        self.list_positions1 = LIST_POSITIONS1
        self.list_positions2 = LIST_POSITIONS2
        self.list_positions3 = LIST_POSITIONS3
        self.list_positions4 = LIST_POSITIONS4
        self.list_squares1 = []
        self.list_squares2 = []
        self.list_squares3 = []
        self.list_squares4 = []
        self.create_wall()


    def create_wall(self):
        for i in range(len(self.list_positions1)):
            new_square = Turtle()
            new_square.hideturtle()
            new_square.speed(-1)
            new_square.penup()
            new_square.shape("square")
            new_square.shapesize(0.8, 2)
            new_square.color("#00ADAB")
            new_square.goto(self.list_positions1[i])
            new_square.showturtle()
            self.list_squares1.append(new_square)

        for i in range(len(self.list_positions2)):
            new_square = Turtle()
            new_square.hideturtle()
            new_square.speed(-1)
            new_square.penup()
            new_square.shape("square")
            new_square.shapesize(0.8, 2)
            new_square.color("#D61C4E")
            new_square.goto(self.list_positions2[i])
            new_square.showturtle()
            self.list_squares2.append(new_square)

        for i in range(len(self.list_positions3)):
            new_square = Turtle()
            new_square.hideturtle()
            new_square.speed(-1)
            new_square.penup()
            new_square.shape("square")
            new_square.shapesize(0.8, 2)
            new_square.color("#E5A510")
            new_square.goto(self.list_positions3[i])
            new_square.showturtle()
            self.list_squares3.append(new_square)

        for i in range(len(self.list_positions4)):
            new_square = Turtle()
            new_square.hideturtle()
            new_square.speed(-1)
            new_square.penup()
            new_square.shape("square")
            new_square.shapesize(0.8, 2)
            new_square.color("#8E9D20")
            new_square.goto(self.list_positions4[i])
            new_square.showturtle()
            self.list_squares4.append(new_square)