#!usr/bin/env python
#####
# chris romero
# political trivia game
#####

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file)

    points = next_line(the_file)

    return category, question, answers, correct, explanation, points

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\tWelcome to Political Trivia Challenge 2017!\n")
    print("\t\t", title, "\n")

def judgement(score):
    if score > 1 and score <= 10:
        print("You got one or two correct answers :|.")

    elif score > 10 and score <= 20:
        print("You got a few right, try again!")
        
    elif score > 20 and score <= 50:
        print("You got some correct answers... You know some things :)")

    elif score > 50 and score <= 69:
        print("You got a majority correct...")

    elif score >= 70 and score < 100:
        print("You passed, but it wasn't perfect... Try again.")

    elif score == 100:
        print("You got every question correct, hooray! You know your political trivia :)")

    elif score == 0:
        print("You got a zero but that's ok, try again!")
        
 
def main():
    trivia_file = open_file("trivia_points.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nCorrect!", end=" ")
            score += int(points)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation, points = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)
    judgement(score)
 
main()  
input("\n\nPress the enter key to exit.")

        
