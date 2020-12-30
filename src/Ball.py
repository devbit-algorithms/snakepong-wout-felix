import turtle

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(40)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = -5
        self.ball.dy = -5
    def resetBall(self):
        self.ball.goto(0, 0)
    def ckeckcollisionBall(self):
        if self.ball.ycor() > 280:
            self.ball.sety(280)
            self.ball.dy *= -1

        # DOWN WALL
        if self.ball.ycor() < -280:
            self.ball.sety(-280)
            self.ball.dy *= -1

        # RIGTH WALL
        if self.ball.xcor() > 480:
            self.ball.setx(480)
            self.ball.dx *= -1

        if self.ball.xcor() < -480:
            self.ball.setx(-360)
            self.ball.dx *= -1
            return True
    def movementBall(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
    def checkCollitionWithPeddal(self,paddle):
        if (self.ball.xcor() < -360 and self.ball.xcor() > - 370 and ((self.ball.ycor() < paddle.ycor() + 40) and (self.ball.ycor() > paddle.ycor() - 40))):
            self.ball.setx(-360)
            self.ball.dx *= -1
    def checkCollitionWithTail(self,segments):
        for segment in segments:
            if (segment.distance(self.ball) < 20):
                self.ball.dx *= -1
                self.ball.dy *= -1
    def getBall(self):                  #only here for testing
        return self.ball
    def SetBallDirection(self,x,y):     #only here for testing
        self.ball.setx(x)
        self.ball.sety(y)
