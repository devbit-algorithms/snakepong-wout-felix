import turtle


class Sketch:

    def Setup(self):
        self.sketch = turtle.Turtle() 
        self.sketch.speed(0) 
        self.sketch.color("blue") 
        self.sketch.penup() 
        self.sketch.hideturtle() 
        self.sketch.goto(0, 260)
        return self.sketch
    def write(self, score):
        self.sketch.write("Score : {}".format(score),
			align="center", font=("Courier", 24, "normal"))

    def clear(self):
        self.sketch.clear()