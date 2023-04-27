import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

i = 0

while game_is_on:
    time.sleep(0.1)
    if i % (6 - scoreboard.level) == 0:
        car_manager.create_car()
    for car in car_manager.car_list:
        car_manager.scroll(car)
        if player.distance(car) < 35 and car.ycor() - 20 <  player.ycor() < car.ycor() + 20:
            scoreboard.you_lose()
            game_is_on = False
        if player.ycor() > 280:
            scoreboard.level_up()
            car_manager.level += 1
            player.reset()
        car_manager.check_loc(car)
    i += 1
    screen.update()
 
screen.exitonclick()