#!/usr/bin/python3

def main():
    round = 0
    answer = " "

    while round < 3 and answer != "Brian":
        round += 1     # increase the round counter by 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        if answer.capitalize() == "Brian": # logic to check if user gave correct answer
            print("Correct!")
            break
        elif answer.capitalize() == "Shrubbery":
            print("That is a great choice")
            break
        elif round == 3:    # logic to ensure round has not yet reached 3
            print("Sorry, the answer was Brian.")
            break
        else:                 # if answer was wrong
            print("Sorry. Try again!")

main()
