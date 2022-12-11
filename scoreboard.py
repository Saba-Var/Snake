from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(align="center", font=("Arial", 20, "normal"),
                   arg=f"Score: {self.score} || High Score: {self.high_score}")

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
