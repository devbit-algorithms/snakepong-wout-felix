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