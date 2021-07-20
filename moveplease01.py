#!/usr/bin/env python3

import shutil
import os

def movefiles():
    #setting starting directory
    os.chdir('/home/student/mycode/')

    #moving file to the ceph_storage directory
    shutil.move('raynor.obj', 'ceph_storage/')
    #get name for kerrigan.obj
    xname = input('What is the new name for kerrigan.obj?')
    #rename kerrigan.obj to something else
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

movefiles()

