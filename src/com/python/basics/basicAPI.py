'''
Created on 16-May-2018

@author: pratyusk
'''
import time
from __builtin__ import input, str


# add a and b
def add(a, b):
    return a + b

    
# Subtract b from a
def subtract(a, b):
    return a - b


# Returns current time
def whatTimeIsIt():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime

#reads input from user and prints on screen
def readInputFromUser():
    name = raw_input("Please type your name: ");
    print "Hi ", name
