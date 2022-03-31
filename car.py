from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(300, random.randint(-250, 250))
        self.color("#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)]))
        self.setheading(180)

    def move(self, speed):
        self.forward(speed)