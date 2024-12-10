###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################



stage.set_background("nature.png")

q1 = codesters.Circle(100, 100, 200, 'green')
q1 = codesters.Square(100, -100, 200, 'purple')
q1 = codesters.Square(-100, 100, 200, 'red')
q1 = codesters.Square(-100, -100, 200, 'blue')

s1 = codesters.Sprite("soccerball.gif", 100, 100)
s2 = codesters.Sprite("cardinal", -100, 100)
s1.set_size(2)
s3 = codesters.Sprite("zelda.jpg", -100, -100)
s3.set_size(0.35)
s4 = codesters.Sprite("ramen.jpeg", 100, -100)
s4.set_size(0.7)
message1 = codesters.Text("I like food and soccer",0,-220,"black")