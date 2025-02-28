# section 1 setup
import codesters,random
from codesters import StageClass
import time
stage = StageClass()
stage.disable_all_walls()
player = codesters.Sprite("shark2")
stage.set_background("underwater")
object = codesters.Sprite("fish")
seconds = 120
player.set_size(0.2)
player.goto(-190, 0)
object_speed = -5
score = 0



# section 2 objects
def falling_object():
    global object_speed, score, seconds, time
    seconds -= 2

    if seconds == 0:
        player.say(f"your score is {score}", 5)
        
    if seconds > 0 :

        x=200
        y=random.randint(-200, 200)
        object = codesters.Sprite("fish",x,y)

        object.set_size(0.4)
        object.set_x_speed(object_speed)
        
stage.event_interval (falling_object, 2)

# section 3 collision
def collision(player,object):
    global score

    if object.get_image_name()=="fish":
        stage.remove_sprite(object)
        score+=1
        

player.event_collision(collision)


# Section 4 - Controls
def go_up():
    player.move_up(5)

player.event_key("up", go_up)

def go_down():
    player.move_down(5)

player.event_key("down", go_down)