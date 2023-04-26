from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []
        self.level = 0
    

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid = 1, stretch_len = 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-250, 280))
        self.car_list.append(new_car)

    
    def scroll(self, car):
        car.backward(STARTING_MOVE_DISTANCE + (self.level * MOVE_INCREMENT))
      


    def check_loc(self, car):
        if car.xcor() < -300:
            car.hideturtle()
            self.car_list.remove(car)
