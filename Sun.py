import turtle

class Sun:
    def __init__(self):
        self.pen = turtle.Pen()
        self.pen.speed(10)

    def draw(self, size, color):
        self.pen.pendown()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        self.pen.circle(size)
        self.pen.end_fill()

