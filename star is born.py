import turtle

turtle.shape("turtle")

turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()

turtle.speed(100)

size = 0


def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


star(turtle, 75)


for i in range(60):
    star(turtle, 75)
    turtle.right(5)
    size += 3

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()


size = 0


def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


star(turtle, 75)


for i in range(60):
    star(turtle, size)
    turtle.right(5)
    size += 3

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()


size = 0


def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


star(turtle, 75)


for i in range(60):
    star(turtle, size)
    turtle.right(5)
    size += 3


turtle.exitonclick()

