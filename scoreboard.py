from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-230, 270)
        self.color("Black")
        self.refresh()

    def level_up(self):
        self.level += 1

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", font = FONT, align = ALIGNMENT, move=False)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font = FONT, align = ALIGNMENT, move=False)