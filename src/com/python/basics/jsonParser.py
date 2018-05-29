'''
Created on 28-May-2018

@author: pratyusk
'''

data = {}
data["a"] = { "name" : "aRam",
            "phone" : 9837892379847892
    }
data["b"] = { "name" : "bRam",
            "phone" : 9837892379847891
    }
import json
s=json.dumps(data)
print s  
print type(data) , type(s)
