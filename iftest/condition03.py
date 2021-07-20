#!/usr/bin/env python3`

def main():
    # create the string hostname
    hostname = "MTG"
    # test logic with the `if` statement
    # what to do if this statement is found to be true
    if hostname == "MTG":
        print("The hostname was found to be mtg")

def part2():
    #get a name
    hostname = input("What is the hostname?")
    if hostname.lower() == "mtg":
        print("The hostname is mtg")
        print("The hostname matches the expected config.")
    else:
        print("The hostname is not mtg")

main()
part2()
print("The program has completed")
