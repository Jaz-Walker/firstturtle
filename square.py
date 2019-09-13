import turtle


turtle.shape("turtle")

turtle.speed(10)

size = 3

def square(turtle, sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)


for i in range(60):
    square(turtle,75)
    turtle.right(5)

size += 3
turtle.exitonclick()
