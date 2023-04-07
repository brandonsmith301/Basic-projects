from turtle import Turtle
import random

class Food(Turtle): # inheriting turtle class
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup() # removes pen
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color('yellow')
        self.speed('fastest') # so we can't see food being created
        
        
    def refresh(self):
        random_x = random.randint(-250, 250) 
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
        
        