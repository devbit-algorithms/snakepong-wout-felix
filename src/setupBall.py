import turtle


class Ball:

    def setupBall(self):
        ball = turtle.Turtle()
        ball.speed(40)
        ball.shape("circle")
        ball.color("red")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = -5
        ball.dy = -5
        return ball