from turtle import Turtle


# Turtle Player

class Myturtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.tilt(90)
        self.penup()
        self.goto(0,-280)

    def up_move(self):
        my_pos = self.ycor() + 10
        self.goto(0,my_pos)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial",14,"normal"))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-380,270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}",align="left",font=("Courier", 14, "normal"))

    def increase_level(self):
        self.level +=1
        self.update_score()
