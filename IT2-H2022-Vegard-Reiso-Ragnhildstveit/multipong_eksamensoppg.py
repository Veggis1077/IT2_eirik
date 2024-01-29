

import turtle
import random
import time

wn = turtle.Screen()
wn.title("Pong by @Veggis1077 and @Mikal037")
wn.bgcolor("black")
wn.setup(width=450, height=600)
wn.tracer(0)
""" turtle.Screen() lager skjermen, 
setter den til svart
bredde og høyde(800, 600)
tracer slik at en kan stoppe spille elns vet ikke helt"""

# Score


# Padlle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.color("purple")
paddle_a.penup()
paddle_a.goto(0, -230)



farger = ["white", "orange", "red", "purple", "blue", "pink", "yellow", "green"]


class Ball:
    def __init__(self):
        self.farge = random.choice(farger)
        self.xstart = random.randint(-100, 100)
        self.yStart = random.randint(0, 200)
        # Ball
        self.balll = turtle.Turtle()
        self.balll.speed(0)
        self.balll.shape("circle")
        self.balll.color(self.farge)
        self.balll.penup()
        self.balll.goto(self.xstart, self.yStart)
        self.dx = round(random.uniform(0.05, 0.8), 2) * random.choice([-1, 1])
        self.dy = round(random.uniform(0.25, 0.6), 2) * random.choice([-1, 1])

    def side(self):
        ball = self.balll
        ball.setx(ball.xcor() + self.dx)
        ball.sety(ball.ycor() + self.dy)

        # border checking
        if ball.ycor() > 290:
            ball.sety(290)
            self.dy *= -1

        if ball.xcor() > 210:
            ball.setx(210)
            self.dx *= -1

        if ball.xcor() < -210:
            ball.setx(-210)
            self.dx *= -1

        if (ball.ycor() < -210 and ball.ycor() > -220) and (
                ball.xcor() < paddle_a.xcor() + 50 and ball.xcor() > paddle_a.xcor() - 50):
            ball.sety(-210)
            self.dy *= -1


""" beveger seg alltid 2 piksler i hver retning"""

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Antall tap: 0", align="center", font=("comic Sans MS", 24, "normal"))


# functions

def paddle_a_up():
    x = paddle_a.xcor()
    x += 35
    paddle_a.setx(x)


# keybord binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
""".listen gjør at den følger med på hva du gjør med tastaturet
onkeypress utførere en funksjon når riktig key er flyttet"""


def paddle_a_down():
    x = paddle_a.xcor()
    x -= 35
    paddle_a.setx(x)


wn.listen()
wn.onkeypress(paddle_a_up, "Right")
wn.onkeypress(paddle_a_down, "Left")

# Main game loop
objs = [Ball() for i in range(2)]

# objs[0].do_sth()
tid = time.time()
n = 0
score = 0
while True:
    wn.update()
    dt = time.time() - tid

    if (dt > 5):
        tid = time.time()
        objs.append(Ball())
    for a in objs:
        a.side()
        if (a.balll.ycor() > -210 and a.balll.ycor() < -208):
            score += 10
        else:
            pass

        if a.balll.ycor() < -300:
            objs.remove(a)
            n += 1

    pen.clear()
    pen.write("antall tap {} /10".format(n), align="center", font=("Courier", 24, "normal"))

    if n == 10:
        pen.clear()
        pen.goto(0, 0)
        pen.write(
            f"!Du har tapt Looser¡ \n Takk for at du spilte spillet til \n @Veggis1077 og Mikal037\n \n Din score ble {score} ",
            align="center", font=("Courier", 18, "normal",))
        time.sleep(10)
        break