#!/usr/bin/env python3

def main():
    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:
        # create list of lines
        dnslist = dnsfile.readlines()
        # loop over lines
        for svr in dnslist:
            #print and end without a newline
            print(svr, end="")


main()
