from turtle import Turtle
import random

class Ball(Turtle): # inheriting turtle class
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup() # removes pen
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        
    def refresh(self):
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move 
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1 # to reverse the ball
        
    def bounce_x(self):
        self.x_move *= -1 # to reverse the ball
        