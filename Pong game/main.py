from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor('black')
s.title("Brandon's Pong game")
s.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = Scoreboard()

s.listen()

# for the right paddle
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")

# for the left paddle
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.5)
    s.update() 
    ball.move() 
    
    # creating collision with wall
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # collision with right paddle
    elif ball.distance(r_paddle) < 100 and ball.xcor() > 340:
        ball.bounce_x()
        
    # collision with left paddle
    elif ball.distance(l_paddle) < 100 and ball.xcor() < -340:
        ball.bounce_x()
        
    # out of bounds
    elif ball.xcor() == -450:
        score.P2_increase_score()
        ball.refresh()
        
    # out of bounds
    elif ball.xcor() == 450:
        score.P1_increase_score()
        ball.refresh()
        
    

s.exitonclick()