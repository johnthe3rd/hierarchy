#!/usr/bin/env python
import os, sys, glob


#a script for moving around in and illustrating directory hierarchy
dirs = []

try:
    base = sys.argv[1]
    if base[-1] != '/':
        base += '/'
    dirs.append(base)
except IndexError:
    dirs.append(os.getcwd() + '/')


#def getdirs(x):
#        for i in os.listdir(x):
            

print dirs
