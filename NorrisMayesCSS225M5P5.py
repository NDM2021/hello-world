import turtle

wn = turtle.Screen()
wn.bgcolor("Red")
alex = turtle.Turtle()
alex.color("Blue")
alex.shape("turtle")

print(list(range(3, 8, 5)))
alex.up()
for size in range(3, 8, 5):
    alex.stamp()
    alex.forward(size)
    alex.right(6)

wn.exitonclick()

# Norris Mayes
# 2/19/20
# This program draws for the user
