import turtle


class Ball:
    def setupBall(self):
        self.ball = turtle.Turtle()
        self.ball.speed(40)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = -5
        self.ball.dy = -5
        return self.ball
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