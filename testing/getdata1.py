#!/usr/bin/env python
""" test for importing apps/scripts"""
import json
import requests


def mainfunction():
    jsondata = requests.get("http://api.open-notify.org/astros.json")
    print(jsondata)
    print(type(jsondata))

if __name__ == "__mainfunction__":
    mainfunction()
