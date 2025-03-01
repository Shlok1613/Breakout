from turtle import Turtle


class Wall:
    def __init__(self, color, start_pos_y):
        self.bricks1 = []
        self.bricks2 = []
        start_pos_x = -280
        for _ in range(13):
            brick_row1 = Turtle()
            brick_row1.shape("square")
            brick_row1.color(color)
            brick_row1.shapesize(stretch_len=2, stretch_wid=1)
            brick_row1.penup()
            brick_row1.goto(start_pos_x, start_pos_y)

            self.bricks1.append(brick_row1)

            brick_row2 = Turtle()
            brick_row2.shape("square")
            brick_row2.color(color)
            brick_row2.shapesize(stretch_len=2, stretch_wid=1)
            brick_row2.penup()
            brick_row2.goto(start_pos_x, start_pos_y - 25)

            self.bricks2.append(brick_row2)
            start_pos_x += 46
