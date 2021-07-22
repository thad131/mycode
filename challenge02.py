#!/usr/bin/env python
"""trying out challenge #2"""
import requests


def main():
    """Main function doing everything"""
    jsondata = requests.get("http://api.open-notify.org/astros.json")
    astros = jsondata.json()
    print("here is the data for astronauts in space: \n")
    print(astros['people'])
    print("current status in readable format:")
    for naut in astros['people']:
        print(naut['name'] + " is onboard the " + naut['craft'])
    print("app complete")

main()
