#!/usr/bin/env python3

def main():
    ipchk = input("Apply an IP address: ") # this line now prompts the user for input
    #Testing the value
    if ipchk:
       print("Looks like the IP address was set: " + ipchk) # indented under if
    else:    # if data is NOT provided
       print("You did not provide input.") # indented under else

#run the main function
main()
