import random
import queue
import time
from pynput import keyboard

# coordinates as [x,y] (horizontal,vertical)

class field:
    def __init__(self,size,apples_target):
        self.size = size #coordinates
        self.apples = [] #list of coordinates, appended till apples_target is reached
        self.apples_target = apples_target #specifies how many apples there shall be

    def apples_spawn(snake):
        while len(self.apples) < self.apples_target:
            newapple = [random.randint(1,self.size[0]),random.randint(1,self.size[1])]
            if newapple not in snake.tail and newapple != snake.position:
                self.apples.append(newapple)

    def check_for_eaten_apples(snake):
        for apple in self.apples[:]:
            if apple == snake.position:
                self.apples.remove(apple)



class snake:
    def __init__(self, position, length, direction, alive, tail):
        self.position = position #list (coordinates)
        self.length = length #int
        self.direction = direction #string
        self.alive = alive #bool
        self.tail = tail #list of previous coordinates, number of coordinates is length -1

    def move(self,):
        movemap = {
            "right": [1,0],
            "up": [0,1],
            "left": [-1,0],
            "down": [0,-1]
        }
        positional_change = movemap[self.direction]
        self.position = [self.position[0] + positional_change[0], self.position[1] + positional_change[1]]

    def check_for_death (self,field):
        if self.position[0] or self.position[1] <= 0:
         self.alive = False
        if self.position[0] > field.size[0] or self.position[1] > field.size[1]:
         self.alive = False
        if self.position in self.tail:
         self.alive = False

    def check_input():



def gameloop(snake,field):
    while snake.alive == True:
        snake.move()
        check_for_death(snake,field)

def check

#main

size = #extract it from config db

field = field()

snake_position = [int(field_width),int(field_height)]
snake_lenght = 2
dirmap = {
    1: "right",
    2: "up",
    3: "left",
    4: "down"
} #global
snake_direction = dirmap[random.randint(1,4)]
snake_alive =

snake = snake()
