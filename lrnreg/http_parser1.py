#!/usr/bin/env python3

import urllib.request
import re



def main():
    print("Where should we search?")
    url = input()
    repeat = "n"
    while repeat == "n":
        print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
        searchFor = input()
        searchMe = urllib.request.urlopen(url).read().decode("utf-8")
        if re.search(searchFor, searchMe):
            print("Found a match!")
        else:
            print("No match.")
        repeat = input('Perform another search on ' + url +"?")

if __name__ == '__main__':
    main()
