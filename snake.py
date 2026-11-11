import random
import queue
import time
#from pynput import keyboard
import sqlite3

# coordinates as [x,y] (horizontal,vertical)

class fieldclass:
    def __init__(self,size,apples_target):
        self.size = size #coordinates
        self.apples = [] #list of coordinates, appended till apples_target is reached
        self.apples_target = apples_target #specifies how many apples there shall be

    def apples_spawn(self,snake):
        while len(self.apples) < self.apples_target:
            newapple = [random.randint(1,self.size[0]),random.randint(1,self.size[1])]
            if newapple not in snake.tail and newapple != snake.position and newapple not in self.apples:
                self.apples.append(newapple)

    def check_for_eaten_apples(self,snake):
        for apple in self.apples[:]:
            if apple == snake.position:
                self.apples.remove(apple)
                snake.length = snake.length + 1

    def render(self,snake):
        canvas = ""
        counter1 = 0
        counter2 = 0
        while counter1 <= self.size[1] + 1:
            while counter2 <= self.size[0]+1:
                pos = [counter2,counter1]
                if pos in snake.tail:
                    symbol = '*'
                elif pos == snake.position:
                    symbol = "0"
                elif pos in self.apples:
                    symbol = "+"
                elif not (self.size[0] >= counter1 > 0 and self.size[1] >= counter2 > 0):
                    symbol = "#"
                else:
                    symbol = " "
                canvas = canvas + symbol
                counter2 = counter2 + 1
            counter1 = counter1 + 1
            canvas = canvas + "\n"
            counter2 = 0
        print(canvas)

class snakeclass:
    def __init__(self, position, length, direction, alive, tail):
        self.position = position    #list (coordinates)
        self.length = length        #int
        self.direction = direction  #string
        self.alive = alive          #bool
        self.tail = tail            #list of previous coordinates, number of coordinates is length -1.
                                    #the nearest position to the head will be at the and with the append method, the furthest, end of the tail will be 0 so that i can always pop 0 and delete the end.

    def move(self,):
        movemap = {
            "right": [1,0],
            "up": [0,1],
            "left": [-1,0],
            "down": [0,-1]
        }
        positional_change = movemap[self.direction]
        #save the position of the head to be added to the tail
        prev_position = self.position
        #update actual position
        self.position = [self.position[0] + positional_change[0], self.position[1] + positional_change[1]]
        self.update_tail(prev_position)

    def update_tail (self, previous):
        #this function assumes that the tail is a list of coordinates with the indexes 0 to length -2.
        #the number of coordinates is self.length - 1
        #this function appends the previous position (given from the move method
        #use the pop method until the list has the desired length
        #end of the list is the head end, low indexes are the tail end of the snake
        tail_length = self.length - 1
        self.tail.append(previous)
        while len(self.tail) > tail_length:
            self.tail.pop(0)


    def check_for_death (self,field):
        if self.position[0] <= 0 or self.position[1] <= 0:
            self.alive = False
        if self.position[0] > field.size[0] or self.position[1] > field.size[1]:
            self.alive = False
        if self.position in self.tail:
            self.alive = False

    def check_input(self):
        opposites =
        valid_command = False
        while valid_command == False:
            command = input(">")
            if command == "":
                return
            if command in ["right","left","up","down"]:
                self.direction = command
                valid_command = True
            else:
                print("nahhh")


def gameloop(snake,field):
    while snake.alive == True:
        field.render(snake)
        snake.check_input()
        snake.move()
        snake.check_for_death(field)
        field.check_for_eaten_apples(snake)
        field.apples_spawn(snake)

#main

size = [20,20]
apples = 3

snake_position = [size[0]/2,size[1]/2]
snake_length = 2
dirmap = {
    1: "right",
    2: "up",
    3: "left",
    4: "down"
} #global
snake_direction = dirmap[random.randint(1,4)]
snake_alive = True

snake = snakeclass(snake_position, snake_length, snake_direction, snake_alive, [])
field = fieldclass(size,3)

gameloop(snake,field)
