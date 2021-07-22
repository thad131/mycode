#!/usr/bin/env python3

import requests
import pandas as pd
import json
import csv

def getrows(data):
    # ?? this totally depends on what's in your data
    return []

def translate(r,file):
    with open(file,'wb') as csvf:
        outcsv = csv.writer(csvf)
        outcsv.writerows(getrows(r))

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://api.magicthegathering.io/v1/sets')
    file = "test_api.csv"
    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    translate(r,file)
    print(r)
    print(r.json())
    #for catfact in r.json():
    #    print(catfact.get("text"))  # the .get() method returns NONE if key not found



if __name__ == '__main__':
    main()
