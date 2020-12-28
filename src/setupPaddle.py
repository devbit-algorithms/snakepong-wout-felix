import turtle


class Paddle:

    def paddle(self):
        paddle = turtle.Turtle()
        paddle.shape("square")
        paddle.speed(0)
        paddle.shapesize(stretch_wid = 6, stretch_len = 2)
        paddle.penup()
        paddle.goto(-400, 0)
        return paddle