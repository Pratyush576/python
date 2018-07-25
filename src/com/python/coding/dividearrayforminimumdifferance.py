'''
Created on 16-Jun-2018

@author: pratyusk

https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

Partition a set into two subsets such that the difference of subset sums is minimum. 
Given a set of integers, the task is to divide it into two sets S1 and S2 such that 
the absolute difference between their sums is minimum.

'''


def minDiff(list1, setSize, startIndex, endIndex, s):
    global MIN
    
    # print list1, setSize, startIndex, endIndex, s
    if(setSize == 0 or startIndex >= endIndex):
        return abs(sum(list1) - 2 * s)
    for index in range(startIndex, endIndex):
        m1 = minDiff(list1, setSize - 1, startIndex, index - 1, s + list1[index])
        m2 = minDiff(list1, setSize - 1, index + 1, endIndex, s + list1[index])
        # print m1 , m2
        if m1 > m2:
            if MIN > m1:
                MIN = m1
        else:
            if MIN > m2:
                MIN = m2
    return MIN          


MIN = 10000
serstr =""

list = [3, 1, 4, 2, 2, 1]#[54, 66, -31, 54, 22, 34, 43, 50, -17]
length = len(list)
print length , length / 2
print range(1, length / 2)
for size in range(1, length / 2 + 1):
    print "=================Size:", size
    minDiff(list, size, 0, length - 1, 0)
    print "@@@MIN: ", MIN
