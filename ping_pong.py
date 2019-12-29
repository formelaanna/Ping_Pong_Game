import turtle
import time
from time import sleep

window = turtle.Screen()
window.title("PONG GAME")
window.bgcolor("teal")
window.setup(width=900, height=700)
window.tracer(0)

# Left paddle
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("gray")
pad_a.shapesize(stretch_wid=6, stretch_len=1)
pad_a.penup()
pad_a.goto(-420, 0)

# Right paddle
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("gray")
pad_b.shapesize(stretch_wid=6, stretch_len=1)
pad_b.penup()
pad_b.goto(420, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# ball.dx = 0.2
# ball.dy = 0.2

ball.dx = 5
ball.dy = 5

# Result
score_a = 0
score_b = 0

# score information
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center", font=("Courier", 24, "normal"))


# Paddles movement options

def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)


def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)


def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)


# Keybord settings

window.listen()
window.onkeypress(pad_a_up, "w")
window.onkeypress(pad_a_down, "s")
window.onkeypress(pad_b_up, "Up")
window.onkeypress(pad_b_down, "Down")

FPS = 30
frameDelay = 1000 / FPS

# Ball movements options
while True:

    frameStart = int(round(time.time() * 1000))

    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1  # reversing direction

    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1

    if ball.xcor() > 440:
        score_a += 1
        ball.goto(0, 0)  # center position
        ball.dx *= -1
        pen.clear()
        pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -440:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center",
                  font=("Courier", 24, "normal"))

    if (
            ball.xcor() > 390 and ball.xcor() < 400) and ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40:
        ball.setx(390)
        ball.dx *= -1

    if (
            ball.xcor() < -390 and ball.xcor() > -400) and ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40:
        ball.setx(-390)
        ball.dx *= -1
    afterTime = int(round(time.time() * 1000))

    frameTime = afterTime - frameStart

    if (frameDelay > frameTime):
        sleep((frameDelay - frameTime) / 1000)


