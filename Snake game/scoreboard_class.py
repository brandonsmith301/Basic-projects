from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Volumes/GoogleDrive/My Drive/Self projects (learning)/Snake game/scores.txt") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write((f"SCORE: {self.score} HIGH SCORE: {self.high_score}"), False, align=ALIGN, font=(FONT))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('/Volumes/GoogleDrive/My Drive/Self projects (learning)/Snake game/scores.txt', mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

        