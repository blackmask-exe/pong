import turtle
from turtle import Turtle


class Paddle:
    def __init__(self, xcord, ycord):
        self.paddle = Turtle()
        self.xcord = xcord
        self.ycord = ycord
        self.create_paddle()

    def create_paddle(self):
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.teleport(self.xcord, self.ycord)
        self.paddle.penup()

    def slider_up(self):
        self.paddle.sety(self.paddle.ycor() + 20)

    def slider_down(self):
        self.paddle.sety(self.paddle.ycor() - 20)
