from turtle import Turtle

FONT = ("Courier", 50, "normal")
brick_points = {
    "red": 7,
    "orange": 5,
    "yellow": 1,
    "green": 3
}


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.score = 0
        self.update_lives()
        self.update_scores()

    def update_lives(self):
        self.goto(150, 260)
        self.write(self.lives, align="center", font=FONT)

    def lives_lost(self):
        self.clear()
        self.lives -= 1
        self.update_lives()
        self.update_scores()

    def update_scores(self):
        self.goto(-150, 260)
        self.write(self.score, align="center", font=FONT)

    def new_score(self, brick_color):
        self.clear()
        if brick_color in brick_points:
            self.score += brick_points[brick_color]
        self.update_scores()
        self.update_lives()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def win(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=FONT)
