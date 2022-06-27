from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.score = 0
        self.penup()
        self.goto(position)
        self.write(f"{self.score}", False, "center", ("Georgia", 50, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "center", ("Georgia", 50, "normal"))


