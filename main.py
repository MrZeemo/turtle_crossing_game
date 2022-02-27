from turtle import Turtle, Screen
import time
from player import Player
from cars import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("gray")
screen.tracer(0)
screen.screensize(600, 600)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finishline():
        scoreboard.add_score()
        player.refresh()
        car_manager.level_up()









screen.exitonclick()