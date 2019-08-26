import turtle
import math

class Tree:

    def __init__(self):
        self.pen = turtle.Pen()
        self.pen.speed(10)
        self.pen.penup()
        self.half_size = 0

    def height_of_triangle(self, half_base):
        height = 0
        full_base = half_base * 2
        height_squared = math.pow(full_base, 2) - math.pow(half_base, 2)
        height = math.sqrt(height_squared)
        return height


    def draw(self, size):

        self.half_size = size/2

        self.pen.pendown()

        self.pen.fillcolor("brown")
        self.pen.begin_fill()

        self.pen.left(90)
        self.pen.forward(size)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(size)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(size)
        self.pen.right(90)
        self.pen.forward(25)

        self.pen.end_fill()

        #Green branches
        #area of triangle: Area = half * base * height
        #perimeter = side + side + side
        #height^2 = a^2 - b^2
        #Height 173.2050807568877
        #first
        self.pen.fillcolor("green")
        self.pen.begin_fill()
        self.pen.forward(self.half_size)
        for i in range(2):
            self.pen.left(120)
            self.pen.forward(size)
        self.pen.left(120)
        self.pen.forward(self.half_size)
        self.pen.end_fill()

        #second move up
        self.pen.penup()
        self.pen.left(90)
        height = self.height_of_triangle(size/2)
        size = height * 0.8
        self.half_size = size/2
        self.pen.forward(size)
        self.pen.right(90)
        self.pen.pendown()

        #second draw
        self.pen.fillcolor("green")
        self.pen.begin_fill()
        self.pen.forward(self.half_size)
        for i in range(2):
            self.pen.left(120)
            self.pen.forward(size)
        self.pen.left(120)
        self.pen.forward(self.half_size)
        self.pen.end_fill()

        # third move up
        self.pen.penup()
        self.pen.left(90)
        height = self.height_of_triangle(size / 2)
        size = height * 0.8 #adjusting the variables to make triangle smaller
        self.half_size = size / 2 #adjusting the variables to make triangle smaller
        self.pen.forward(size)
        self.pen.right(90)
        self.pen.pendown()

        # third draw
        self.pen.fillcolor("green")
        self.pen.begin_fill()
        self.pen.forward(self.half_size)
        for i in range(2):
            self.pen.left(120)
            self.pen.forward(size)
        self.pen.left(120)
        self.pen.forward(self.half_size)
        self.pen.end_fill()




