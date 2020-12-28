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
screen.setup(width = 1000, height = 600)

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
ClassBall = Ball()
ball = ClassBall.setupBall()

# Global part

#Sets key bindings to the right thing.
bindings = Bindings(screen,snakehead,paddle)
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
    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    

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
        segments[0].goto(x,y)

    move.move(snakehead)

    # ALL NEXT CODE ARE COLLISIONS
    
    # Collision detection with borders
    if snakehead.xcor() > 490 or snakehead.xcor() < -350 or snakehead.ycor() > 290 or snakehead.ycor() < -290:
        time.sleep(0.5)
        snakehead.goto(0,0)
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
        ball.goto(0, 0)

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

            # Reset the start_tail
            tail.clear_start_tail_var()
            # Reset the score
            score = 0

            # Reset the ball
            ball.goto(0, 0)

    # Check for collision of ball with borders
    # UP WALL
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    # DOWN WALL
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # RIGTH WALL
    if ball.xcor() > 480:
        ball.setx(480)
        ball.dx *= -1

    # LEFT WALL
    # When the ball hits the left wall, the snake expands one element on the tail
    if ball.xcor() < -480:
        tail.add_tail(segments)
        ball.setx(-360)
        ball.dx *= -1
        score += 1
        sk.clear()
         
        
    # Collision of the ball with the paddle
    if (ball.xcor() < -360 and ball.xcor() > - 370 and ((ball.ycor() < paddle.ycor() + 40) and (ball.ycor() > paddle.ycor() - 40))):
        ball.setx(-360)
        ball.dx *= -1

    # Collision with ball and the tail of the snake
    # When you go with your snake through your ball or go sideways the ball goes back in reverse way
    # Sometimes when you go through the ball, this next code is executed twice because it makes two contacts with the snake
    for segment in segments:
        if (segment.distance(ball) < 20):
            ball.dx *= -1
            ball.dy *= -1

    time.sleep(delay)

screen.mainloop()