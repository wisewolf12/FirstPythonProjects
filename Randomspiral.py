import random
import turtle
import tkinter.colorchooser
t = turtle.Pen()
t.speed(0)
#k = input("What background color would you like?(enter color name only)")
k = tkinter.colorchooser.askcolor(color=None)
print("k type is ",type(k))

turtle.bgcolor(k[1])


colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
z = int(input("How many spirals would you like?(enter number only)"))
a = int(input("Enter an angle for your spirals(be creative,but remember to enter a number only"))

for n in range(z):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(a)
