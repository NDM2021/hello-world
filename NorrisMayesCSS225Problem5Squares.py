import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of 10 sides"""
    for i in range(4):
        t.forward(10)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

wn.exitonclick()

# Norris Mayes
# 3/2/20
# This code is turned into a function and draw it.
