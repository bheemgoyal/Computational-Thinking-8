import random

#pick a word at random
word_list = ["pizza", "stuff", "globs", "words", "fluff" "About", "Alert", "Argue",	"Beach","Above", "Alike", "Arise", "Began", "Abuse", "Alive", "Array", "Begin", "Actor", "Allow", "Aside", "Begun", "Along", "Audio, "Below", "Adopt" "Alter", "Audit", "Bench","Adult", "Among", "Avoid" "Billy", "After", "Anger"]
hidden_word = random.choice(word_list)

# repeat for six guesses
for i in range (6):
    #guess a word
    guess_word = input()
    output = ""

    # first letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # first letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # first letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # first letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # first letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"


    # result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("you win")
        break

print(f"you used {i+1} guesses")
