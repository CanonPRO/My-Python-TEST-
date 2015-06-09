#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
@Author: CanonPRO
@Data: 2015-6-10
"""

print ('*' * 30)
username = raw_input ("Enter your name: ")
userfami = raw_input ("Enter this last name: ")
userage = raw_input ("Enter the age of: ")
usrcity = raw_input ("Enter your city: ")
ma = raw_input ("Are you married? (y/n): ")
if ma == 'y':
	mb = raw_input ("Enter the name of his wife: ")
print ('*' * 30)
print (" ")
print ('*' * 30)
print ("Briefly about you:")
print (" ")
print ("Your name: " + username)
print ("Your last name: " + userfami)
print ("You: " + userage)
print ("You from: " + usrcity)
print ("Your wife's name: " + mb)
print ('*' * 30)
