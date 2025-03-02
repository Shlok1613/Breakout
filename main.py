from turtle import *
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

#-----------------Main Game--------------------#
game_is_on = True
while game_is_on:

    if scoreboard.lives == 0:
        game_is_on = False
        scoreboard.game_over()

    #Ball Movement and start
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with side and upper walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.reverse_x()
    if ball.ycor() > 330:
        ball.reverse_y()

    #Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -300:
        ball.reverse_y()

    #Ball miss by paddle
    if ball.ycor() < -345:
        ball.start()
        paddle.start()
        scoreboard.lives_lost()
        ball.move_speed = 0.1

    #Detect collision with bricks
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

            # Get brick boundaries
            brick_left = brick.xcor() - 20
            brick_right = brick.xcor() + 20
            brick_top = brick.ycor() + 10
            brick_bottom = brick.ycor() - 10

            ball_x = ball.xcor()
            ball_y = ball.ycor()

            # Determine collision side
            if brick_left < ball_x < brick_right:
                # Vertical collision (top or bottom)
                ball.reverse_y()

            elif brick_bottom < ball_y < brick_top:
                # Horizontal collision (left or right)
                ball.reverse_x()

            # Hide the brick and increase ball speed
            brick.hideturtle()
            brick.goto(1000, 100)
            ball.move_speed *= 0.9

        else:
            scoreboard.win()

screen.exitonclick()
