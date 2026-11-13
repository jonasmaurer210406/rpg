import time

class field:
    size=[20,20]
    apples=[[3,2],[16,4],[5,13]]


class snake:
    position=[10,10]
    tail=[[10,11],[10,12],[11,12],[12,12]]

def render(field,snake):
    canvas = ""
    counter1 = 0
    counter2 = 0
    while counter1 <= field.size[1] + 1:
        while counter2 <= field.size[0] + 1:
            pos = [counter2,counter1]
            if pos in snake.tail:
                 symbol = '*'
            elif pos == snake.position:
                symbol = "0"
            elif pos in field.apples:
                symbol = "+"
            elif not (field.size[0] >= counter1 > 0 and field.size[1] >= counter2 > 0):
                symbol = "#"
            else:
                symbol = " "
            canvas = canvas + symbol
            counter2 = counter2 + 1
        counter1 = counter1 + 1
        canvas = canvas + "\n"
        counter2 = 0
    print(canvas)

counter = 0
frametimes = []
start = time.time()
render(field,snake)
end = time.time()
frametime = end - start
print(f"Frametime: {frametime} seconds")
#frametimes.append(frametime)
#counter += 1
#average_frametime = sum(frametimes) / len(frametimes)
#average_fps = 1 / average_frametime
#
#print(f"average Frametime: {average_frametime} \naverage FPS: {average_fps}")
#
