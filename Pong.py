from sys import set_coroutine_origin_tracking_depth
import turtle

wn = turtle.Screen()
wn.title("Ping Pong by Uday Chandra")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("lightgreen")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("lightgreen")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("lightgreen")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Score System
score_a = 0
score_b = 0


# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("AI: 0 Player: 0", align = "center", font=("Century Gothic", 20, "normal"))

# Functions
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding For Paddle
wn.listen()
wn.onkeypress(paddle_b_up, "w")
wn.onkeypress(paddle_b_down, "s")

# Main Game Loop
while True:
    wn.update()

    # Ai Paddle (Paddle A)
    if ball.xcor() > -330:
        paddle_a.sety(ball.ycor())

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("AI: {} Player: {}".format(score_a, score_b), align = "center", font=("Century Gothic", 20, "normal"))

    if score_a > 10:
        pen.write("The Ai wins!")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("AI: {} Player: {}".format(score_a, score_b), align = "center", font=("Century Gothic", 20, "normal"))

    if score_b > 10:
        pen.write("You win!")

    if paddle_b.ycor() < -235:
        paddle_b.sety(paddle_b.ycor() + 1 + 0.999)

    if paddle_b.ycor() > 245:
        paddle_b.sety(paddle_b.ycor() - 1 - 0.999)

    # Paddle and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1    



