import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manage=CarManager()
score_board=Scoreboard()

screen.listen()
screen.onkeypress(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manage.create_cars()
    car_manage.car_move()

    for car in car_manage.all_cars:
        if car.distance(player)<20:
            score_board.game_over_screen()
            game_is_on=False


    #detect if the player has reached to the top or not
    if(player.is_player_at_top()):
        player.reset_position()
        car_manage.car_speedup()
        score_board.level_up()



screen.exitonclick()