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


def listProcessing():
    list = [1, 5, 23, 54, 22, 34, 66, 54, 75]
    for i in range(len(list)):
        print list[i]
    print list[1:4]
    print list[5:]


# Returns current time
def whatTimeIsIt():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime


# reads input from user and prints on screen
def readInputFromUser():
    name = raw_input("Please type your name: ");
    print "Hi ", name


# Returns temperature in fahrenheit
def KelvinToFahrenheit(Temperature):
    return ((Temperature - 273) * 1.8) + 32
  
  
# 100 will be divided by number and result would be printed 
def tryExceptDemo(number):
    try:
        i = 100 / number
    except ZeroDivisionError:
        print "Numbers can't be devide by zero"
    else:
        print "Number after division: ", i

        
# 100 will be divided by number and result would be printed 
def tryExceptFinllyDemo(number):
    try:
        i = 100 / number
    except ZeroDivisionError:
        print "Numbers can't be devide by zero"
    else:
        print "Number after division: ", i
    finally:
        print "finally block will always be executed!!!"


def StringBasics():
    str = "abcdefedcba"
    print str
    print "Reverse of String is ", str[::-1]
    if str == str[::-1]:
        print "String is palindrome"


class basics:
    
    def __init__(self, name):
        print "Name is ", name

    def test(self):
        print "test api in basics class"

