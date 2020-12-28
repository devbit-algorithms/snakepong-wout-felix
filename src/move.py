import turtle


class Move:

    def move(self, snakehead):
        if snakehead.direction == "up":
            y = snakehead.ycor()
            snakehead.sety(y + 20)

        if snakehead.direction == "down":
            y = snakehead.ycor()
            snakehead.sety(y - 20)

        if snakehead.direction == "left":
            x = snakehead.xcor()
            snakehead.setx(x - 20)

        if snakehead.direction == "right":
            x = snakehead.xcor()
            snakehead.setx(x + 20)
