#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

def main():
    calc1 = 0.0
    calc2 = 0.0
    
    operation = ""
    while (calc1 != "q"):
        print("\nWhat is the first operator? Or, enter q to quit: ")
        q = input("What is Q?")
        calc1 = float(calc1)
        
        calc2 = float(calc2)
        if calc1 == "q":
            break
        
        print("\nWhat is the second operator? Or, enter q to quit: ")
        #calc2 = raw_input()
        if calc2 == "q":
            break
        #calc1 = raw_input()
        print("Enter an operation to perform on the two operators (+ or -): ")
        if operation == "+":
            print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
        elif operation == '-':
            print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
        else:
            print("\n Not a valid entry. Restarting...")

main()
