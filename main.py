import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
l_scoreboard = Scoreboard("left")
r_scoreboard = Scoreboard("right")

# line_drawer = Turtle()
# line_drawer.color("white")
# line_drawer.goto(-350, -330)
# line_drawer.goto(-350, 300)

# slider moving mechanism


screen.listen()
screen.onkey(key="w", fun=l_paddle.slider_up)
screen.onkey(key="s", fun=l_paddle.slider_down)
screen.onkey(key="Up", fun=r_paddle.slider_up)
screen.onkey(key="Down", fun=r_paddle.slider_down)

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    # wall bounce:
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_bounce()
    # paddle bounce:
    r_paddle_upper_bound = r_paddle.paddle.ycor() + 50
    r_paddle_lower_bound = r_paddle.paddle.ycor() - 50
    l_paddle_upper_bound = l_paddle.paddle.ycor() + 50
    l_paddle_lower_bound = l_paddle.paddle.ycor() - 50

    if 340 <= ball.xcor() <= 345:
        if r_paddle_lower_bound <= ball.ycor() <= r_paddle_upper_bound or l_paddle_lower_bound <= ball.ycor() <= l_paddle_upper_bound:
            ball.paddle_bounce()
    if -340 >= ball.xcor() >= -345:
        if r_paddle_lower_bound <= ball.ycor() <= r_paddle_upper_bound or l_paddle_lower_bound <= ball.ycor() <= l_paddle_upper_bound:
            ball.paddle_bounce()
    # out of bounds logic
    if ball.xcor() > 425 or ball.xcor() < -425:
        ball.ball_out_of_bounds()
        if ball.horizontal_speed > 0:
            r_scoreboard.r_score_update()
        elif ball.horizontal_speed < 0:
            l_scoreboard.l_score_update()

        screen.update()
        time.sleep(2)

screen.exitonclick()
