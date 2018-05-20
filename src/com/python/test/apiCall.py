'''
Created on 17-May-2018

@author: pratyusk
'''
from com.python.basics import basicAPI

print "Current Time: ", basicAPI.whatTimeIsIt()
print "Addition of Numbers is: ", basicAPI.add(10, 37)
#basicAPI.readInputFromUser()
print basicAPI.KelvinToFahrenheit(100)
print basicAPI.KelvinToFahrenheit(-100)

print "\n"
basicAPI.tryExceptDemo(20)
basicAPI.tryExceptDemo(0)

print "\n"
basicAPI.tryExceptFinllyDemo(20)
basicAPI.tryExceptFinllyDemo(0)

print "\n"
base=basicAPI.basics("Pratyush")
base.test()