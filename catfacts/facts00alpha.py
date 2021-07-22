#!/usr/bin/env python3

import requests


def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # display the methods available to our new object
    print( dir(r) )



if __name__ == '__main__':
    main()
