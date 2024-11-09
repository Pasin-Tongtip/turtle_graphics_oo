import random
import turtle


class Polygon:
    def __init__(self):
        self.__num_sides = random.randint(3, 5)
        self.__size = random.randint(50, 150)
        self.__orientation = random.randint(0, 90)
        self.__location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.__border_size = random.randint(1, 10)
        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    @property
    def num_sides(self):
        return self.__num_sides

    @num_sides.setter
    def num_sides(self, new_sides):
        self.__num_sides = new_sides

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, new_orientation):
        self.__orientation = new_orientation

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        self.__location = new_location

    @property
    def border_size(self):
        return self.__border_size

    @border_size.setter
    def border_size(self, new_border):
        self.__border_size = new_border

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    def draw_polygon(self):
        num = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))
        if num == 1:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(3):
                    turtle.forward(self.__size)
                    turtle.left(360 / 3)
                turtle.penup()
        elif num == 2:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(4):
                    turtle.forward(self.__size)
                    turtle.left(360 / 4)
                turtle.penup()
        elif num == 3:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(5):
                    turtle.forward(self.__size)
                    turtle.left(360 / 5)
                turtle.penup()
        elif num == 4:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(self.__num_sides):
                    turtle.forward(self.__size)
                    turtle.left(360 / self.__num_sides)
                turtle.penup()
        elif num == 5:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(3):
                    turtle.forward(self.__size)
                    turtle.left(360 / 3)
                reduction_ratio = 0.618
                turtle.penup()
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                self.__location[0] = turtle.pos()[0]
                self.__location[1] = turtle.pos()[1]
                self.__size *= reduction_ratio
                turtle.penup()
        elif num == 6:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(4):
                    turtle.forward(self.__size)
                    turtle.left(360 / 4)
                reduction_ratio = 0.618
                turtle.penup()
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                self.__location[0] = turtle.pos()[0]
                self.__location[1] = turtle.pos()[1]
                self.__size *= reduction_ratio
                turtle.penup()
        elif num == 7:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(5):
                    turtle.forward(self.__size)
                    turtle.left(360 / 5)
                reduction_ratio = 0.618
                turtle.penup()
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                self.__location[0] = turtle.pos()[0]
                self.__location[1] = turtle.pos()[1]
                self.__size *= reduction_ratio
                turtle.penup()
        elif num == 8:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(self.__num_sides):
                    turtle.forward(self.__size)
                    turtle.left(360 / self.__num_sides)
                reduction_ratio = 0.618
                turtle.penup()
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                self.__location[0] = turtle.pos()[0]
                self.__location[1] = turtle.pos()[1]
                self.__size *= reduction_ratio
                turtle.penup()
        else:
            for i in range(30):
                turtle.penup()
                turtle.goto(self.__location[0], self.__location[1])
                turtle.setheading(self.__orientation)
                turtle.color(self.__color)
                turtle.pensize(self.__border_size)
                turtle.pendown()
                for _ in range(self.__num_sides):
                    turtle.forward(self.__size)
                    turtle.left(360 / self.__num_sides)
                reduction_ratio = 0.618
                turtle.penup()
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(self.__size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                self.__location[0] = turtle.pos()[0]
                self.__location[1] = turtle.pos()[1]
                self.__size *= reduction_ratio
                turtle.penup()


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
draw = Polygon()
draw.draw_polygon()
turtle.done()
