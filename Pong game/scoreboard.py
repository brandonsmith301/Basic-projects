from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write((f"P1: {self.left_score} | P2: {self.right_score}"), False, align=ALIGN, font=(FONT))
        
    def P1_increase_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()
        
    def P2_increase_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()