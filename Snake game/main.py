from turtle import Turtle, Screen
import time
from snake_class import Snake
from snake_food import Food
from scoreboard_class import Scoreboard

# creating snake with class
snake = Snake()
food = Food()
score = Scoreboard()

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('black')
s.tracer(0)
s.title("Brandon's Snake Game")

#applying keystrokes to snake game
s.listen()
s.onkey(snake.up,'Up')
s.onkey(snake.down,'Down')
s.onkey(snake.left,'Left')
s.onkey(snake.right,'Right')

# to make the snake move
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    s.update() 
    snake.move()   
    
    # to detect collision with food
    if snake.head.distance(food) <18:
        food.refresh()
        score.increase_score()
        snake.extend()
        
    #detect collision
    if snake.head.xcor() > 310 or snake.head.xcor() < -310 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
        score.reset()
        snake.reset()
            
        
    #detect collision with tail
    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
        
            
            
            
            
s.exitonclick()