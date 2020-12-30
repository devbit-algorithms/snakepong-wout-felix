from Ball import Ball


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