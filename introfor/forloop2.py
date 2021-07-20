#!/usr/bin/env python3
# create the list called vendors

def main():
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
    # loop across the list vendors
    # create a second list of strings
    approved_vendors = ["cisco", "juniper", "big_ip"]
    for x in vendors:
        print("The vendor is " + x, end="")  # each time through the loop print value of x
        if x not in approved_vendors:
            print("Not an approved Vendor")
    print("\nOur loop has ended.")  # when the loop ends print this

main()

