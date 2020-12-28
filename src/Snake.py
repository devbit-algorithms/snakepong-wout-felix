import turtle


class Snake:

    def snakehead(self):
        snakehead = turtle.Turtle()
        snakehead.shape("square")
        snakehead.speed(40)
        snakehead.penup()
        snakehead.goto(0,0)
        snakehead.direction = "right"
        return snakehead