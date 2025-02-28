# section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)

def move_left(sprite):
    sprite.move_left(1)

def move_right(sprite):
    sprite.move_right(1)

# section 2: bind controls to specific keys
s1.event_key("left", move_left)
s1.event_key("right", move_right)
def show(sprite):
    sprite.show()
s1.event_key("g", show)