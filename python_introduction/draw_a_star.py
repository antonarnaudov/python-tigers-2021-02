import turtle

t = turtle.Turtle()
t.pensize(5)

length = 5

for cont in range(100):
    t.forward(length)

    t.right(135)
    length = length + 5
