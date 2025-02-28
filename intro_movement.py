# section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)


# Section2: define controls
def move_up(sprite):
    sprite.move_up(1)

def move_down(sprite):
    sprite.move_down(1)

def move_left(sprite):
    sprite.move_left(1)

def move_right(sprite):
    sprite.move_right(1)


# Section 3: define hide and show
def hide(sprite):
    sprite.hide()


# section 4: bind controls to specific keys
s1.event_key("up", move_up)
s1.event_key("down", move_down)
s1.event_key("left", move_left)
s1.event_key("right", move_right)
s1.event_key("h", hide)
def show(sprite):
    sprite.show()
s1.event_key("g", show)

# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")

def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading = sprite.heading
    sprite.set_heading(heading - 1)

def forward(sprite):
    sprite.forward(1)


s1.event_key("l", turn_right)
s1.event_key("j", turn_left)
s1.event_key("i", forward)
    
def draw(sprite):
    sprite.pen_down()

s1.event_key("d", draw)

def stop_drawing(sprite):
    sprite.pen_up()

s1.event_key("u", stop_drawing)

def erase(sprite):
    sprite.pen_clear()

s1.event_key("e", erase)

def red_pen(sprite):
    sprite.set_color("red")

s1.event_key("r", red_pen)

def green_pen(sprite):
    sprite.set_color("green")

s1.event_key("g", green_pen)

def blue_pen(sprite):
    sprite.set_color("blue")

s1.event_key("b", blue_pen)

def yellow_pen(sprite):
    sprite.set_color("yellow")

s1.event_key("y", yellow_pen)

def orange_pen(sprite):
    sprite.set_color("orange")

s1.event_key("o", orange_pen)

def purple_pen(sprite):
    sprite.set_color("purple")

s1.event_key("p", purple_pen)


