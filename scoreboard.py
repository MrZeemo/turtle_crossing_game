from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 250)
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.update_score()

    def update_score(self):
        self.write(f"Level : {self.level}", align="center", font=(FONT))


    def add_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write("GameOver", align="center", font=(FONT))






