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
    if hostname == "MTG":
        print("The hostname is mtg")
    else:
        print("The hostname is not mtg")

main()
part2()
