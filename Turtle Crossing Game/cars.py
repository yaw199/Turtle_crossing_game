from turtle import Turtle
import random


COLORS = ["red","blue","yellow","purple","green","orange","pink","teal"]


class Car():
    def __init__(self):
        self.all_cars = []
            

    def car_shape(self):
        rand_shape = random.randint(1,5)
        if rand_shape == 2:
            cr = Turtle("square")
            cr.shapesize(2,1)
            cr.settiltangle(90)
            cr.penup()
            cr.color(random.choice(COLORS))
            randy = random.randint(-240,240)
            cr.goto(400,randy)
            self.all_cars.append(cr)
            
                  

    def move_left(self):
        for each_car in self.all_cars:
            posx = each_car.xcor() - 10
            each_car.setx(posx)
            