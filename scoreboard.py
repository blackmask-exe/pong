from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.penup()
        self.hideturtle()
        self.sety(250)
        self.color("white")
        if side == "left":
            self.setx(-200)
            self.write(arg=f"Score: {self.lscore}", font=("Arial", 20, "normal"))
        elif side == "right":
            self.setx(80)
            self.write(arg=f"Score: {self.rscore}", font=("Arial", 20, "normal"))

    def l_score_update(self):
        self.lscore += 1
        self.clear()
        self.write(arg=f"Score: {self.lscore}", font=("Arial", 20, "normal"))

    def r_score_update(self):
        self.rscore += 1
        self.clear()
        self.write(arg=f"Score: {self.rscore}", font=("Arial", 20, "normal"))
