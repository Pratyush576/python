'''
Created on 16-Jun-2018

@author: pratyusk

WAP to return kth magic number where magic number is defined as M=5^m+s^n and m,n>=0
'''


def getMagicNumber(k):
    m = 0
    n = 0
    index = 1
    if k == index:
        print m,n
        return 5 ** m + 5 ** n
    while True:
        if m == n:
            m=0
            n += 1
        else:
            m += 1
        index += 1
        if index == k:
            print m,n
            return 5 ** m + 5 ** n

print getMagicNumber(1)
print getMagicNumber(3)
print getMagicNumber(6)
print getMagicNumber(100)