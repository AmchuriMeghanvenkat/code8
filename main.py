import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy=Player()
screen.listen()
screen.onkey(timmy.go_up,"Up")
screen.onkey(timmy.go_down,"Down")
scoreboard=Scoreboard()
car_manager=CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.creat_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(timmy)<20:
            game_is_on=False
            scoreboard.game_over()
    if timmy.is_at_finsh_line():
        timmy.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()