import turtle
import time
from Keyboard_bindings import Bindings
from Snake import Snake
from Paddle import Paddle
from Border import Border
from Ball import Ball
from move import Move
from Tail import Tail
from sketch import Sketch

delay = 0.001
start_tail = 1
score = 0
# Set up the screen
screen = turtle.Screen()
screen.setup(width=1000, height=600)

# SNAKE PART
# Snake head
snake = Snake()
snakehead = snake.snakehead()
# long border
bor = Border()
border = bor.setUpBorder()
# Snake tail
segments = []
# Paddle
# You can move the paddle with 'z' and 's'
pad = Paddle()
paddle = pad.paddle()
# Ball of circle shape
Ball = Ball()

# Global part
#Sets key bindings to the right thing.
bindings = Bindings(screen, snakehead, paddle)
bindings.Keyboard_bindings()
#movement of the snakehead
move = Move()
move.move(snakehead)
tail = Tail()
semgents = tail.add_tail(segments)
# Displays the score
sk = Sketch()
sketch = sk.Setup()

# Main game loop
while True:

    screen.update()
    #updates the scoreboard
    sk.write(score)
    Ball.movementBall()
    # sets the start tail to three
    tail.start_tail(segments)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x, y)

    move.move(snakehead)
    # Collision detection with borders
    if snakehead.xcor() > 490 or snakehead.xcor() < -350 or snakehead.ycor() > 290 or snakehead.ycor() < -290:
        time.sleep(0.5)
        snakehead.goto(0, 0)
        snakehead.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the start_tail
        tail.clear_start_tail_var()

        # Reset the score
        score = 0

        # Reset the ball
        # ball.goto(0, 0)
        Ball.resetBall()

    # Check for snakehead collision with the tail segments
    for segment in segments:
        if segment.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0, 0)
            snakehead.direction = "right"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the start_tail
            tail.clear_start_tail_var()
            # Reset the score
            score = 0

            # Reset the ball
            Ball.resetBall()

    # Check for collision of ball with borders
    # UP WALL
    #returns true if it colides with the left wall
    # LEFT WALL
    # When the ball hits the left wall, the snake expands one element on the tail
    if Ball.ckeckcollisionBall():
        tail.add_tail(segments)
        score += 1
        sk.clear()

    # Collision of the ball with the paddle
    Ball.checkCollitionWithPeddal(paddle)
    # Collision with ball and the tail of the snake
    # When you go with your snake through your ball or go sideways the ball goes back in reverse way
    # Sometimes when you go through the ball, this next code is executed twice because it makes two contacts with the snake
    Ball.checkCollitionWithTail(segments)
    time.sleep(delay)

screen.mainloop()
