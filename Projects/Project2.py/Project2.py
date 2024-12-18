###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


while True:
    word = input("What do you think grandma likes? ")

    if "z" in word:
        print(f"Grandma doesn't like {word}!")
    else:
        print(f"Grandma likes {word}")

    print("")