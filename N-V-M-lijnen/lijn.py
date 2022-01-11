import turtle




def main(lengte,q):
    punt = turtle.Turtle()
    punt.color("grey")
    def Basis(lengte,q):
        Lengte_balk = lengte ##
        Scharnier_a = 0
        Scharnier_b = Lengte_balk
        punt.forward(Lengte_balk)
        Scharnier()
        punt.left(135)
        punt.penup()
        punt.forward(Lengte_balk)
        punt.right(180)
        punt.pendown()
        Scharnier()
        punt.left(45)
        if q == True:
            q_last(Lengte_balk)


    def Scharnier():
        punt.begin_fill()
        punt.right(45)
        punt.forward(20)
        punt.right(135)
        punt.forward(30)
        punt.right(135)
        punt.forward(20)
        punt.end_fill()

    def q_last(Lengte_balk):
        punt.forward(50)
        punt.right(90)
        punt.forward(Lengte_balk)
        punt.right(90)
        punt.forward(50)
    Basis(lengte,q)
    turtle.done()
