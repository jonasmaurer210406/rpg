import random

# coordinates as [x,y] (horizontal,vertical)

class snake:
    def __init__(self, position, length, direction, alive, tail):
        self.position = position #list (coordinates)
        self.length = length #int
        self.direction = direction #string
        self.alive = alive #bool
        self.tail = tail #list of previous coordinates, number of coordinates is length -1

    def move(self):
        movemap = {
            "right": [1,0],
            "up": [0,1],
            "left": [-1,0],
            "down": [0,-1]
        }
        positional_change = movemap[self.direction]
        self.position = [self.position[0]+positional_change[0],self.position[1]+positional_change[1]]

def check_for_death(field, snake):
    if snake.position[0] or snake.position[1] < 0:
        snake.alive = False
    if snake.position in snake.tail:
        snake.alive = False

def gameloop(snake):
    while snake.alive == True:
        move()

field_height = 40
field_width = 40

# init snake
snake_position = [int(field_width),int(field_height)snake_lenght = 1]
snake_lenght = 2
dirmap = {
    1: "right",
    2: "up",
    3: "left",
    4: "down"
} #global
snake_direction = dirmap[random.randint(1,4)]
snake_alive = True
