#!/usr/bin/env python3

import requests


def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    print(r)
    print(r.json())



if __name__ == '__main__':
    main()
