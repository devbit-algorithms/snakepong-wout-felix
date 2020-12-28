import turtle


class Border:

    def setUpBorder(self):
        border = turtle.Turtle()
        border.shape("square")
        border.speed(0)
        border.shapesize(stretch_wid = 40, stretch_len = 0.5)
        border.penup()
        border.goto(-360, 0)
        return border