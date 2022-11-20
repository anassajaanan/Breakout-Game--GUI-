from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from score import Score


# ==========Screen================
window = Screen()
window.title("Breakout Game")
window.bgcolor("#E7E7E5")
window.screensize()
window.setup(600, 600)
window.tracer(0)

# ============Paddle==================
paddle = Paddle()
# ==============Ball==================
ball = Ball()
# ==============Wall==================
wall = Wall()
# =============Score==================
score = Score()



window.listen()
window.onkey(paddle.move_right, 'Right')
window.onkey(paddle.move_left, 'Left')

game_is_on = True
while game_is_on:
    window.update()
    ball.move_ball()
    if ball.xcor() < paddle.xcor() + 60 and ball.xcor() > paddle.xcor() - 60:
        if ball.ycor() < paddle.ycor() + 10:
            ball.sety(ball.ycor())
            ball.dy *= -1


    for i in range(len(wall.list_squares1)):
        if ball.distance(wall.list_squares1[i]) <= 25:
            ball.sety(ball.ycor())
            ball.dy *= -1
            wall.list_squares1[i].reset()
            wall.list_squares1[i].hideturtle()
            wall.list_squares1[i].penup()
            wall.list_squares1[i].goto(900, 900)
            score.add_score(30)

    for i in range(len(wall.list_squares2)):
        if ball.distance(wall.list_squares2[i]) <= 25:
            ball.sety(ball.ycor())
            ball.dy *= -1
            wall.list_squares2[i].reset()
            wall.list_squares2[i].hideturtle()
            wall.list_squares2[i].penup()
            wall.list_squares2[i].goto(900, 900)
            score.add_score(20)

    for i in range(len(wall.list_squares3)):
        if ball.distance(wall.list_squares3[i]) <= 25:
            ball.sety(ball.ycor())
            ball.dy *= -1
            wall.list_squares3[i].reset()
            wall.list_squares3[i].hideturtle()
            wall.list_squares3[i].penup()
            wall.list_squares3[i].goto(900, 900)
            score.add_score(10)

    for i in range(len(wall.list_squares4)):
        if ball.distance(wall.list_squares4[i]) <= 25:
            ball.sety(ball.ycor())
            ball.dy *= -1
            wall.list_squares4[i].reset()
            wall.list_squares4[i].hideturtle()
            wall.list_squares4[i].penup()
            wall.list_squares4[i].goto(900, 900)
            score.add_score(5)


    if ball.ycor() < paddle.ycor() - 20:
        ball.hideturtle()
        score.game_over()

    if score.score == 585:
        score.win()










