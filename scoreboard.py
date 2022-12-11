from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.high_score = self.get_high_score() or 0
        self.goto(0, 250)
        self.update_scoreboard()
        self.get_high_score()

    def get_high_score(self):
        with open("./high_score.txt") as file:
            high_score = int(file.read())
            return high_score

    def update_scoreboard(self):
        self.clear()
        self.write(align="center", font=("Arial", 20, "normal"),
                   arg=f"Score: {self.score} || High Score: {self.high_score}")

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
