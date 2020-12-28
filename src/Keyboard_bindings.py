import turtle
import time


class Bindings:

    def __init__(self, screen, snakehead, paddle):
        self.screen = screen
        self.snakehead = snakehead
        self.paddle = paddle

    def Keyboard_bindings(self):
        self.screen.listen()
        self.screen.onkeypress(self.go_up, "Up")
        self.screen.onkeypress(self.go_down, "Down")
        self.screen.onkeypress(self.go_right, "Right")
        self.screen.onkeypress(self.go_left, "Left")
        self.screen.onkeypress(self.paddleup, "z")
        self.screen.onkeypress(self.paddledown, "s")



    def go_up(self):
        if self.snakehead.direction != "down":
            self.snakehead.direction = "up"

    def go_down(self):
        if self.snakehead.direction != "up":
            self.snakehead.direction = "down"

    def go_left(self):
        if self.snakehead.direction != "right":
            self.snakehead.direction = "left"

    def go_right(self):
        if self.snakehead.direction != "left":
            self.snakehead.direction = "right"

    def paddleup(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def paddledown(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)