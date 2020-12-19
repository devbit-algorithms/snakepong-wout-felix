import turtle
import time

delay = 0.5

# Set up the screen
screen = turtle.Screen()
screen.setup(width=700, height=400)

# Snake head
snakehead = turtle.Turtle()
# snakehead.shape("square")
snakehead.penup()
snakehead.goto(0,0)
snakehead.direction = "stop"

# Functions for example direction
def go_up():
    if snakehead.direction != "down":
        snakehead.direction = "up"

def go_down():
    if snakehead.direction != "up":
        snakehead.direction = "down"

def go_left():
    if snakehead.direction != "right":
        snakehead.direction = "left"

def go_right():
    if snakehead.direction != "left":
        snakehead.direction = "right"

def move():
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

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left, "Left")

# Main game loop
while True:
    screen.update()
    move()

    # Collision detection with borders
    if snakehead.xcor()>340 or snakehead.xcor()<-340 or snakehead.ycor()>190 or snakehead.ycor()<-190:
        time.sleep(0.5)
        snakehead.goto(0,0)
        snakehead.direction = "stop"

    time.sleep(delay)

screen.mainloop()