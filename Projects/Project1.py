###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################



stage.set_background("tree")
q1 = codesters.Square(100, 100, 200, 'green')
q1 = codesters.Square(100, -100, 200, 'purple')
q1 = codesters.Square(-100, 100, 200, 'red')
q1 = codesters.Square(-100, -100, 200, 'blue')
