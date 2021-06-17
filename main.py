import turtle as t


turtle = t.Turtle()
screen = t.Screen()
turtle.color("aqua")


def mov_forwards():
    turtle.forward(10)


def mov_backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=mov_forwards)
screen.onkey(key="s", fun=mov_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
