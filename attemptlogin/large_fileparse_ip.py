#!/usr/bin/env python3
#this library allows us to generate UUID values.

import re

def main():
    # parse keystone.common.wsgi and return number of failed login attempts
    loginfail = 0 # counter for fails
    
    # open the file for reading
    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
    
    # loop over the file
    for line in keystone_file:
    
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
            print(ip)
    print("The number of failed log in attempts is", loginfail)
    keystone_file.close() # close the open file

main()
