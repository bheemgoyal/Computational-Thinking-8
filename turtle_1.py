###############################################
### SETUP ###
import turtle, random
###############################################

#setup
t = turtle.Turtle() 
t.speed(100)
t.penup()
t.goto(-90, -90)
t.color("black")
t.pendown()
colors = ["purple","yellow","blue",]

#turtle draws moving hexagons
for i in range(100):
    t.color( colors[ i % 3 ] )
    t.forward(600 - i)
    t.left(60 - 1)

#turtle repeats moving hexagons in different location
t.goto(300, 300)
for i in range(100):
    t.color( colors[ i % 3 ] )
    t.forward(600 - i)
    t.left(60 - 1)

t.goto(-300, 0)
for i in range(100):
    t.color( colors[ i % 3 ] )
    t.forward(600 - i)
    t.left(60 - 1)

t.goto(50, 100)
for i in range(100):
    t.color( colors[ i % 3 ] )
    t.forward(600 - i)
    t.left(60 - 1)

t.goto(150, 150)
for i in range(100):
    t.color( colors[ i % 3 ] )
    t.forward(600 - i)
    t.left(60 - 1)

t.goto(-150, -100)
for i in range(100):
    t.color( colors[ i % 3 ] )
    t.forward(600 - i)
    t.left(60 - 1)

t.goto(150, 0)
for i in range(100):
    t.color( colors[ i % 3 ] )
    t.forward(600 - i)
    t.left(60 - 1)

t.goto(-250, -200)
for i in range(100):
    t.color( colors[ i % 3 ] )
    t.forward(600 - i)
    t.left(60 - 1)

# ###############################################
### ending ###
turtle.exitonclick()
# ###############################################
