import turtle

turtle.shape("turtle")

turtle.speed(100)

turtle.penup()
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward (300)
turtle.right(90)
turtle.forward(100)
turtle.pendown()
turtle.forward(300)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(170)
turtle.right(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(130)
turtle.penup()
turtle.goto(-240, 50)
turtle.pendown()

size = 0

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


star(turtle, 75)


for i in range(20):
    star(turtle, 75)
    turtle.right(5)
    size += 3

turtle.penup()

turtle.goto(-150, 50)

turtle.pendown()

size = 0

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


star(turtle, 75)


for i in range(15):
    star(turtle, 75)
    turtle.right(5)
    size += 3

turtle.penup()

turtle.goto(100, 150)

turtle.pendown()

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


star(turtle, 75)


for i in range(15):
    star(turtle, 75)
    turtle.right(5)
    size += 3

turtle.penup()
turtle.goto(200,-100)
turtle.pendown()

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


star(turtle, 75)


for i in range(20):
    star(turtle, 75)
    turtle.right(5)
    size += 3

turtle.exitonclick()
