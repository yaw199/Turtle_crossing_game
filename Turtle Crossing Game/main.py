from turtle import Turtle, Screen
from os import system
from player1 import Myturtle,Scoreboard
from cars import Car
import time

system("cls")


my_screen = Screen()
my_screen.setup(width=800,height=600)
my_screen.tracer(0)





# Create turtle

tut_race = Myturtle()


#Create Cars
my_car = Car()
my_score = Scoreboard()


#Listen
my_screen.listen()
my_screen.onkey(tut_race.up_move,"Up")



#Game running

is_running = True
time_sp = 0.2

while is_running:
    time.sleep(time_sp)
    my_screen.update()

    my_car.car_shape()
    my_car.move_left()
    

    if tut_race.ycor() >= 270:
        time_sp *=0.6
        tut_race.goto(0,-280)
        my_car.move_left
        my_score.increase_level()
        time.sleep(time_sp)
        
    
    #Detect collision
    for each_carobject in my_car.all_cars:
        if each_carobject.distance(tut_race) < 23:
            is_running = False
            tut_race.game_over()
            
    



















my_screen.exitonclick()