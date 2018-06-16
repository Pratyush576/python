'''
Created on 16-Jun-2018

@author: pratyusk

https://www.geeksforgeeks.org/replace-every-element-with-the-greatest-on-right-side/
Given an array of integers, replace every element with the next greatest element 
(greatest element on the right side) in the array. Since there is no element next 
to the last element, replace it with -1. For example, if the array is {16, 17, 4, 3, 5, 2}
, then it should be modified to {17, 5, 5, 5, 2, -1}.

'''


def updateArray(arr):
    for i in range(0, len(arr)):
        print "Element: ", arr[i]
        max = -1
        for j in range(i+1, len(arr)):
            if arr[j] > max:
                max = arr[j]
        arr[i] = max
    print arr

    
list = [54, 66, 31, 54, 22, 34, 43, 50, 17]
updateArray(list)
