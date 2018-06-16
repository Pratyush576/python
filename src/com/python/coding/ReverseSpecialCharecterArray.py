'''
Created on 16-Jun-2018

@author: pratyusk
https://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/
Reverse charecter array without effecting special charecter

abc$d  --> dcb$a
'''


def reverseString(str):
    list = toList(str)
    
    print list
    print list[1], len(list)
    l = len(list) - 1
    right = l
    
    for left in range(0, l):
        right -= 1
        
        if not list[right].isalpha():
            print "Special Charecter", list[right]
            right -= 1
        if not list[left].isalpha():
            print "Special Charecter", list[left]
            right += 1
        
        if right <= left :
            break;
        
        x = list[left]
        list[left] = list[right]
        list[right] = x
    print list


# Utility functions
def toList(string):
    List = []
    for i in string:
        List.append(i)
    return List


# list = ["a","b","c","$","d"]
reverseString("abc$d")
