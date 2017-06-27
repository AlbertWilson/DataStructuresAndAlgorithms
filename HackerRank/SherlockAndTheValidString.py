#!/bin/python

import sys
import pdb

def isValid(s):
    dictionary = {}
    for i in s:
    	if dictionary.has_key(i):
    		dictionary[i]+=1
    	else:
    		dictionary[i]=1
    prev=delete=0
    for value in dictionary.values():
    	if prev == 0:
    		prev = value
    	elif prev == value:
    		prev = value
    	elif (abs(value - prev) == 1 or value - 1 == 0) and delete < 1:
    		delete+=1
    	else:
    		return "NO"
    return "YES"

s = raw_input().strip()
result = isValid(s)
print(result)