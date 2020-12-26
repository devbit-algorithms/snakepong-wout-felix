import turtle
import time

delay = 0.5
start_tail = 1

# Set up the screen
screen = turtle.Screen()
screen.setup(width = 1000, height = 600)

# SNAKE PART

# Snake head
snakehead = turtle.Turtle()
snakehead.shape("square")
snakehead.speed(0)
snakehead.penup()
snakehead.goto(0,0)
snakehead.direction = "right"

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.speed(0)
food.penup()
food.goto(0,100)

# Snake tail
segments = []


# Functions for example direction, fruits, ...
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

def add_tail():
    tail_segment = turtle.Turtle()
    tail_segment.speed(0)
    tail_segment.shape("square")
    tail_segment.color("grey")
    tail_segment.penup()
    segments.append(tail_segment)
    

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

# Ball of circle shape
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Main game loop
while True:

    screen.update()

    if start_tail == 1:
        add_tail()
        add_tail()
        add_tail()
        start_tail = 2

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

        # Reset the start_tail
        start_tail = 1

    # Check for collision with food
    if snakehead.distance(food) < 20: # need to change this condition for pong
        # Add a segment
        add_tail()        

        delay -= 0.001

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x,y)

    move()

    # Check for snakehead collision with the tail segments
    for segment in segments:
        if segment.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0,0)
            snakehead.direction = "right"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the delay
            delay = 0.5

            # Reset the start_tail
            start_tail = 1

    time.sleep(delay)

screen.mainloop()