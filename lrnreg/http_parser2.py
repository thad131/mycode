#!/usr/bin/env python3

import urllib.request
import re



def main():
    print("Where should we search?")
    url = input()
    phrase = "nothing"
    searchFor = []
    print("Great! So we'll try to open this url " + str(url) + " to search for the phrase(s):")
    while phrase != "":
        phrase = input()
        searchFor.append= phrase
    for i in searchFor:
        searchMe = urllib.request.urlopen(url).read().decode("utf-8")
        if re.search(i, searchMe):
            print("Found a match for " + i)
        else:
            print("No match for " + i)
    

if __name__ == '__main__':
    main()  
