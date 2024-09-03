from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.vertical_speed = 10
        self.horizontal_speed = 10

    def move(self):
        self.goto(self.xcor() + self.horizontal_speed, self.ycor() + self.vertical_speed)

    def wall_bounce(self):
        self.vertical_speed = self.vertical_speed * -1

    def paddle_bounce(self):
        self.horizontal_speed = self.horizontal_speed * -1

    def ball_out_of_bounds(self):
        self.goto(0, 0)
        self.horizontal_speed = self.horizontal_speed * -1
