#!/usr/bin/python2.7

a = 10
b = 20

list1=[1,2,3,4,5];
if ( a in list1 ):
    print "a is available in the given list"
else:
    print "a is not available in the given list"
if ( b not in list1 ):
    print "b is not available in the given list"
else:
    print "b is available in the given list"
a = 2
if ( a in list1 ):
    print "a is available in the given list"
else:
    print "a is not available in the given list"
