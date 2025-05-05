from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import time

#-------------------Screen Setup----------------#
screen = Screen()
screen.bgcolor("black")
screen.setup(height=700, width=600)
screen.title("Breakout")
screen.tracer(0)

#---------------------All the elements of game--------#
paddle = Paddle()
ball = Ball()
r_wall = Wall("red", 250)
o_wall = Wall("orange", 200)
g_wall = Wall("green", 150)
y_wall = Wall("yellow", 100)
scoreboard = Scoreboard()

#--------------------Key press Detect------------#
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

#-----------------Main Game Loop----------------#
game_is_on = True
while game_is_on:

    if scoreboard.lives == 0:
        game_is_on = False
        scoreboard.game_over()

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with side and upper walls
    if ball.xcor() > 280:
        ball.setx(280)
        ball.reverse_x()
    elif ball.xcor() < -280:
        ball.setx(-280)
        ball.reverse_x()

    if ball.ycor() > 330:
        ball.sety(330)
        ball.reverse_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -310:
        ball.sety(-310)
        ball.reverse_y()

    # Ball missed by paddle
    if ball.ycor() < -345:
        ball.start()
        paddle.start()
        scoreboard.lives_lost()
        ball.move_speed = 0.1

    # Detect collision with bricks
    all_bricks = (
        r_wall.bricks1 + r_wall.bricks2 +
        o_wall.bricks1 + o_wall.bricks2 +
        y_wall.bricks1 + y_wall.bricks2 +
        g_wall.bricks1 + g_wall.bricks2
    )

    for brick in all_bricks:
        if brick.isvisible() and ball.distance(brick) < 25:
            brick_color = brick.color()[0]
            scoreboard.new_score(brick_color)

            brick_left = brick.xcor() - 20
            brick_right = brick.xcor() + 20
            brick_top = brick.ycor() + 10
            brick_bottom = brick.ycor() - 10

            ball_x = ball.xcor()
            ball_y = ball.ycor()

            # Determine collision side
            if brick_left < ball_x < brick_right:
                ball.reverse_y()
            elif brick_bottom < ball_y < brick_top:
                ball.reverse_x()

            brick.hideturtle()
            brick.goto(1000, 100)
            ball.move_speed *= 0.9
            break  # Break after hitting one brick to avoid multiple hits at once

    # Win condition
    if not any(brick.isvisible() for brick in all_bricks):
        scoreboard.win()
        game_is_on = False

screen.exitonclick()
