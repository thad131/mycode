#!/usr/bin/env python3
"""Importing another script"""
import getdata1
from getdata1 import mainfunction



def main():
    """Main function"""
    # open the networktrace (text format)
    print("importing a script")
    mainfunction()
    print("what hapens if I import something and cal main from that???")
    print("end")

if __name__ == '__main__':
    main()
