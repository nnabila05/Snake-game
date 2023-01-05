from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} | High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):

        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w")as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.update_scoreboard()





