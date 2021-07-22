#!/usr/bin/env python3

import requests
import pandas as pd
import json

def csv(json):
    translate = pd.read_json('https://api.magicthegathering.io/v1/sets')
    csv = translate.to_csv
    print(csv)

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://api.magicthegathering.io/v1/sets')
    csv(r)
    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    #print(r)
    #print(r.json())
    #for catfact in r.json():
    #    print(catfact.get("text"))  # the .get() method returns NONE if key not found



if __name__ == '__main__':
    main()
