from Ball import Ball


def test_ball_collitions():
    ball = Ball()
    ball.SetBallDirection(0,290) #has to be over 280, 280 is the wall
    assert ball.getBall().ycor() == 290
    ball.ckeckcollisionBall()
    assert ball.getBall().ycor() == 280 #should of reset 290 to 280
    #assert ball.getBall().dy == -1
