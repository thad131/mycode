#!/usr/bin/env python

import json
import requests


def main():
    jsondata = requests.get("http://api.open-notify.org/astros.json")
    astros = jsondata.json()
    print(astros['people'])
    for naut in astros['people']:
        print(naut['name'] + " is onboard the " + naut['craft'])
    print("app complete")

main()
