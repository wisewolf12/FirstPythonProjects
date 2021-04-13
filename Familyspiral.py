import turtle

t = turtle.Pen()

t.speed(0)
thickness = int(turtle.numinput("Thickness",
                                "How thick do you want your rosette?"))
t.width(thickness)
turtle.bgcolor("black")
colors = turtle.textinput("Enter color", "What color would you like?")

color = turtle.textinput("Enter second color", "What color would you like")

number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles in your rosette?"))

for x in range(number_of_circles):
    t.pencolor(colors)
    t.circle(100)
    t.pencolor(color)

    t.circle(50)
    t.left(360 / number_of_circles)



