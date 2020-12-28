import turtle


class Snake:
    def __init__(self):
      hello = 0

    def snakehead(self):
        snakehead = turtle.Turtle()
        snakehead.shape("square")
        snakehead.speed(40)
        snakehead.penup()
        snakehead.goto(0,0)
        snakehead.direction = "right"
        return snakehead