from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("#2C3637")
        self.speed(-1)
        self.goto(260, 260)
        self.write(f"{self.score}", False, "center", ("Calibri", 30, "bold"))

    def add_score(self, score):
        self.clear()
        self.score += score
        self.penup()
        self.hideturtle()
        self.color("#2C3637")
        self.speed(-1)
        self.goto(260, 260)
        self.write(f"{self.score}", False, "center", ("Calibri", 30, "bold"))


    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("#274299")
        self.speed(-1)
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Calibri", 60, "bold"))

    def win(self):
        self.penup()
        self.hideturtle()
        self.color("#274299")
        self.speed(-1)
        self.goto(0, 0)
        self.write("🎉🎉🎉Congratulation🎉🎉🎉", False, "center", ("Calibri", 40, "bold"))