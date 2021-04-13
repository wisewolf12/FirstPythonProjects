import random
import turtle
t = turtle.Pen()
t.speed(0)
thick = random.randint(1, 10)

turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]


for n in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    sides = random.randint(1, 20)
    thick = random.randint(1, 10)
    angle = t.heading()

    x = random.randrange(0, turtle.window_width()//2)
    y = random.randrange(0, turtle.window_height()//2)
    t.width(thick)
    t.penup()
    t.setpos(x, y)
    t.pendown()

    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 1)
    t.width(thick)
    t.penup()
    t.setpos(-x, y)
    t.pendown()
    t.setheading(180-angle)
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 1)
    t.width(thick)
    t.penup()
    t.setpos(-x, -y)
    t.pendown()
    t.setheading(angle-180)
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 1)
    t.width(thick)
    t.penup()
    t.setpos(x, -y)
    t.pendown()
    t.setheading(360-angle)
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 1)



