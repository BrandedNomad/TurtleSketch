import turtle
import random
from House import *
from Sun import *
from Tree import *

x = 1000
y = 1000

wn =turtle.Screen()


def draw_picture():
    # window

    wn.clearscreen()
    wn.bgcolor("light blue")

    # sun
    sun_size_range = [100,200,150,125,175]
    random_number = random.randint(0,4)
    sun_size = sun_size_range[random_number]
    sun_pos_range = [150 ,100, 0, -100, -150]
    sun_pos = sun_pos_range[random_number]
    sun = Sun()
    sun.pen.penup()
    sun.pen.goto(sun_pos, 100)
    sun.draw(sun_size, "yellow")

    # trees
    positions = [-250, -100, 0, 100, 200]
    sizes = [100, 150, 200, 125, 175]
    tree_amount_range = [1,3,4,5,6,]
    random_number = random.randint(0,4)
    tree_amount = tree_amount_range[random_number]
    random_track = 0
    for i in range(tree_amount):
        random_number = random.randint(0, 4)
        random_track = random_number
        while (random_number == random_track):
            random_number = random.randint(0, 4)
        random_position = positions[random_number]
        tree_size = sizes[random_number]

        tree = Tree()
        tree.pen.goto(random_position, -300)
        tree.draw(tree_size)

    # Houses
    house = House()
    house.pen.penup()
    house.pen.goto(-300, -300)
    size = [100, 50, 200, 25, 75]
    space = [50, 100, 10, 25, 75]
    house_amount_range = [1,2,3,4,5]
    random_number = random.randint(0,4)
    house_amount = house_amount_range[random_number]
    color = ["blue", "orange", "cyan", "purple", "pink"]
    for i in range(house_amount):
        random_number = random.randint(0, 4)
        house_color = color[random_number]
        house_size = size[random_number]
        house_space = space[random_number]
        house.draw(house_size, house_color, house_space)

    wn.listen()
    wn.onkeypress(draw_picture, 'Up')
    wn.mainloop()


draw_picture()

turtle.done()

