import turtle 

t = turtle.Turtle()
t.penup
t.goto(100,0)
t.color("Magenta") 
t.pendown
t.speed(400)

for i in range(500) :
    t.forward(100+i)
    t.left(100+3)
    t.color("red")
    # on line 13 ir make my line red
    t.forward(100+i)
    t.left(100+8)
    t.color("DeepSkyBlue")

turtle.exitonclick()
#on line 11 it make i