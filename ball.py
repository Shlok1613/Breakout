from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("grey")
        self.goto(0, -305)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reverse_x(self):
        self.x_move *= -1

    def reverse_y(self):
        self.y_move *= -1

    def start(self):
        self.goto(0, -305)
        self.reverse_x()
        self.reverse_y()
