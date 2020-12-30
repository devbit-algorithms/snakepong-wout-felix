from Ball import Ball
from Keyboard_bindings import Bindings
import turtle
from Snake import Snake
from Paddle import Paddle



def test_ball_Upwall_collitions():
    ball = Ball()
    ball.SetBallDirection(0,290) #has to be over 280, 280 is the wall
    assert ball.getBall().ycor() == 290
    assert ball.getBall().dy == -5 #
    ball.ckeckcollisionBall()
    assert ball.getBall().ycor() == 280 #should of reset 290 to 280
    assert ball.getBall().dy == 5 #

def test_ball_Down_wall_collitions():
    ball = Ball()
    ball.SetBallDirection(0,-290) 
    assert ball.getBall().ycor() == -290
    assert ball.getBall().dy == -5 
    ball.ckeckcollisionBall()
    assert ball.getBall().ycor() == -280 
    assert ball.getBall().dy == 5 

def test_ball_Right_wall_collitions():
    ball = Ball()
    ball.SetBallDirection(500,0) #has to be over 480, 480 is the wall
    assert ball.getBall().xcor() == 500
    assert ball.getBall().dx == -5 #
    ball.ckeckcollisionBall()
    assert ball.getBall().xcor() == 480 #should of reset 500 to 480
    assert ball.getBall().dx == 5 #

def test_ball_Left_wall_collitions():
    ball = Ball()
    ball.SetBallDirection(-500,0) #has to be over 280, 280 is the wall
    assert ball.getBall().xcor() == -500
    assert ball.getBall().dx == -5 
    assert ball.ckeckcollisionBall() == True
    assert ball.getBall().xcor() == -360 #should reset to -360 since it should reset to the right of the paddle
    assert ball.getBall().dx == 5 #


def test_go_up_keyboard_binding():
    screen = turtle.Screen()
    screen.setup(width=1000, height=600)
    pad = Paddle()
    pad.paddle()
    snakehead = Snake()
    sk = snakehead.snakehead()
    snake = Bindings(screen,sk, pad)
    snake.go_up()
    assert snake.GetsnakeheadDirection() == "up"
    snake.go_right()
    assert snake.GetsnakeheadDirection() == "right"
    snake.go_down()
    assert snake.GetsnakeheadDirection() == "down"
    snake.go_left()
    assert snake.GetsnakeheadDirection() == "left"

    #snake should not go left if it is going right
    snake.go_left()
    snake.go_right()    #should still be going left 
    assert snake.GetsnakeheadDirection() == "left"

    snake.go_up() 
    snake.go_down()#snake should still go up
    assert snake.GetsnakeheadDirection() == "up"



