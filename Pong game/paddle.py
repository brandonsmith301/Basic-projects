from turtle import Turtle
LEN = 1
WID = 5

    
class Paddle(Turtle):
    
    def __init__(self, location):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid = WID, stretch_len = LEN)
        self.penup()
        self.goto(location)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    
        
    
    