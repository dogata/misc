#!/usr/bin/env python3
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <word, value> input file, and move date into 
#  the value field for output
#  
#  Note, this program is written in a simple style and does not full advantage of Python 
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------

desired_channel = 'ABC'

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in = key_value[0]
    value_in   = key_value[1]   #value is 2nd item 

    if value_in.isdigit() | (value_in == desired_channel): # if value is number of views or names of shows only on ABC
        print( '%s\t%s' % (key_in,value_in) )

#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
