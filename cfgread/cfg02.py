#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

def main(configfile):
    ## display file to the screen - .read()
    configblog = configfile.read()

    ## break configblog across line boundaries (strips out \n)
    configlist = configblog.splitlines()

    ## display list with no "\n"
    print(configlist)

    ## Always close your file
    configfile.close()

main(configfile)
