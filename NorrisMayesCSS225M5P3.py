import turtle

wn = turtle.Screen()
sides = int(input("Please enter sides of polygon"))
length_of_sides = int(input("Please enter length of sides of polygon"))
color_of_line = int(input("Please enter color of line of polygon"))
color_of_line = int(input("Blue"))
fill_color = int(input("Please enter fill color of polygon"))
fill_color = int(input("Orange"))

def drawPolygon(t, sideLength, numSides):
     turnAngle = 1080 / numSides
     for i in range(numSides):
          t.forward(sideLength)
          t.right(turnAngle)
          

# Norris Mayes
# 2/18/20
# This code fills and draw polygon
 
