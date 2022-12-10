from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(align="center", font=("Arial", 25, "normal"), arg=f"Score: {self.score}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
