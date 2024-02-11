"""
Quizz game | Documentation

- Guess The Number | w/ Random Library and While loop

    . Some other knowledge applyed in this file are:
        - Style guide PEP-8 for a good syntax and documentation
        - Arithmetic operators
        - Logical operators
        - Conditionals if, else and elif.
"""

#--Random_library
import random


#-Defining the range of numbers
print("Let's define a range of numbers starting from zero to...?")
# This input give us a str()
number_range = input("Type a number: ")



#--Converting the str() into int()
if number_range.isdigit():
    number_range = int(number_range)
    #--Checking if the answear is larger than 0
    if number_range <= 0:
        print("Please choose a number larger than 0 next time...!")
        quit()
else:
    print("Please choose a number next time!")
    quit()



#--Random number
random_library = random.randint  (0, number_range)
#--Number of attemps
guesses = 0



#--Game loop
while True:
    #--Adding number of attemps
    guesses += 1
    #--Game_user_question
    game_question = input("Make a guess: ") #--This input give us a str()

    #--Converting the str() into a int()
    if game_question.isdigit():
        game_question = int(game_question)
    else:
        print("You have to choose a number... Let's try again.")
        continue

    #--Checking if the answear is equal 
    if game_question == random_library:
        print("You got it!")
        break
    #--Checking if the answear is above
    elif game_question > random_library:
        print("You were above")
    #--Checking if the answear is below
    else:
        game_question < random_library
        print("You were below")





#--Converting int() values into str()
final_message = str(guesses) 
#--Showing the message
print("You guess the number in " + final_message + " attemps")