from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f"Level: {self.level}", align= "center", font = FONT)
    
    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def you_lose(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = FONT)