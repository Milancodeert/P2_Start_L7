import turtle
class Koch:
    def __init__(self, start_x, start_y):
        pass
    def teken(self, lengte, hoek):
        turtle.goto(0, 0)
        turtle.forward(lengte)
        turtle.right(hoek)
        turtle.forward(lengte)
        turtle.right(hoek)
        turtle.forward(lengte)




# teken sneeuwvlok
koch1 = Koch(-250, 0)
koch1.teken(3, 250)
koch2 = Koch(koch1.pen.pos()[0], koch1.pen.pos)