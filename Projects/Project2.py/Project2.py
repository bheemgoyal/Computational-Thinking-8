# Beginning of quiz
christmas_points = 0
halloween_points = 0


# Middle of quiz
answer = input("Do you prefer spending time with A) friends, or B) family?")
if answer == "A":
    halloween_points += 1
elif answer == "B":
    christmas_points += 1


answer = input("Do you prefer A) candy, or B) cookies?")
if answer == "A":
    halloween_points += 1
elif answer == "B":
    christmas_points += 1


answer = input("Do you prefer A) scary movies, or B) christmas movies?")
if answer == "A":
    halloween_points += 1
elif answer == "B":
    christmas_points += 1


answer = input("Do you prefer A) costumes, or B) Pjamas?")
if answer == "A":
    halloween_points += 1
elif answer == "B":
    christmas_points += 1


answer = input("Do you prefer A) haunted houses, or B) decorated christmas trees?")
if answer == "A":
    halloween_points += 1
elif answer == "B":
    christmas_points += 1


answer = input("Do you prefer A) spooky stuff, or B) jolly stuff?")
if answer == "A":
    halloween_points += 1
elif answer == "B":
    christmas_points += 1


answer = input("Do you prefer A) exterior decorations, or B) interior decorations?")
if answer == "A":
    halloween_points += 1
elif answer == "B":
    christmas_points += 1


# end of quiz:
if halloween_points > 3:
    print("You are a halloween person")
elif christmas_points > 3:
    print("You are a christmas person")