import turtle

def koch(orde, lengte):
    if orde == 0:
        pen.forward(lengte)
        return
    elif orde > 0:
        koch(orde-1, lengte/3)
        pen.left(60)
        koch(orde - 1, lengte / 3)
        pen.right(120)
        koch(orde - 1, lengte / 3)
        pen.left(60)
        koch(orde - 1, lengte / 3)
        return




pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-250, 0)
pen.pendown()

koch(4, 500)

pen.hideturtle()
turtle.exitonclick()


