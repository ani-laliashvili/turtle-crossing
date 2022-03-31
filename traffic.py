from car import Car
import random

class Traffic:
    def __init__(self):
        self.traffic = []
        self.speed = 10

    def add_cars(self):
        """
        Randomizes the decision to add cars, and randomizes the number of cars to add
        """
        if random.randint(0, 2) == 1:
            new_car = Car()
            self.traffic.append(new_car)

    def move_traffic(self):
        """
        Moves traffic at a given speed
        :param speed:
        """
        for car in self.traffic:
            car.move(self.speed)

    def check_collision(self, turtle_object):
        """
        Checks for collision between any of the cars and the given turtle object
        :param turtle_object: player
        :return: True/False
        """
        for car in self.traffic:
            if car.distance(turtle_object) < 20:
                return True
        return False

    def level_up(self):
        self.speed += 10