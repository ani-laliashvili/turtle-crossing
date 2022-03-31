from turtle import Screen
from player import Player
from traffic import Traffic
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
traffic = Traffic()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    traffic.add_cars()

    # adjust traffic speed based on level
    traffic.move_traffic()

    # check for collision with cars
    if traffic.check_collision(player):
        scoreboard.game_over()
        game_is_on = False

    # check if player has passed the level
    if player.is_at_finish_line():
        traffic.level_up()
        scoreboard.level_up()
        scoreboard.refresh()
        player.reset()

screen.exitonclick()