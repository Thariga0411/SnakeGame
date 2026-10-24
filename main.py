import os
import turtle
import time
import random
delay=0.1
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("pink")
wn.setup(width=600,height=600)
wn.tracer(0) #turn off screen updates
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

def go_up():
    head.direction="up"
def go_down():
    head.direction="down"
def go_left():
    head.direction="left"
def go_right():
    head.direction="right"
def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction =="down":
            y=head.ycor()
            head.sety(y-20)

    if head.direction =="left":
            x=head.ycor()
            head.setx(x-20)

    if head.direction =="right":
            x=head.ycor()
            head.setx(x+20)
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"s")
wn.onkeypress(go_down,"d")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"q")
while True:
    wn.update()
    time.sleep(delay)

    move()
wn.mainloop()