import turtle
import time

delay = 0.5

# Set up the screen
screen = turtle.Screen()
screen.setup(width = 1000, height = 600)

# SNAKE PART

# Snake head
snakehead = turtle.Turtle()
snakehead.shape("square")
snakehead.penup()
snakehead.goto(0,0)
snakehead.direction = "stop"

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(0,100)

# Snake tail
segments = []


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

# PONG PART

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid = 6, stretch_len = 2)
left_paddle.penup()
left_paddle.goto(-400, 0)

# Main game loop
while True:
    screen.update()
    
    

    # Collision detection with borders
    if snakehead.xcor() > 490 or snakehead.xcor() < -490 or snakehead.ycor() > 290 or snakehead.ycor() < -290:
        time.sleep(0.5)
        snakehead.goto(0,0)
        snakehead.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

    # Check for collision with food
    if snakehead.distance(food) < 20:
        # Add a segment
        tail_segment = turtle.Turtle()
        tail_segment.shape("square")
        tail_segment.color("grey")
        tail_segment.penup()
        segments.append(tail_segment)

        delay -= 0.001

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the snakehead is
    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x, y)

    move()

    time.sleep(delay)

screen.mainloop()