

import turtle


class House:

    def __init__(self):
        self.size = 100
        self.space = 50
        self.pen = turtle.Pen()
        self.pen.speed(10)

    def draw(self, size, color, space):

        self.size = size
        self.space = space

        self.pen.pendown()

        #Square
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        for i in range(4):
            self.pen.forward(self.size)
            self.pen.left(90)

        self.pen.left(90)
        self.pen.forward(self.size)
        self.pen.right(90)
        self.pen.end_fill()
        self.pen.forward(self.size)


        #Triangle

        self.pen.fillcolor("red")
        self.pen.begin_fill()
        for i in range(3):
            self.pen.left(120)
            self.pen.forward(self.size)
        self.pen.end_fill()

        self.pen.right(90)
        self.pen.forward(self.size)

        self.pen.penup()
        self.pen.left(90)
        self.pen.forward(space)
        self.pen.pendown()