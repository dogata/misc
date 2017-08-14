#!/usr/bin/env python

# ---------------------------------------------------------------
# This reducer code will input a line of text and output <program, total-views>
# -- Modified to fix missing outputs.
# -- Cases are made explicit.
# ---------------------------------------------------------------
import sys

import os
#myid = 'pipe_test' # UNIX pipe
#myid = os.environ["mapred_tip_id"] # used for debugging
#mylog = open("/Users/HoweXVIIi/online-courses/hadoop/hadoop_debug/"+myid,"w")

last_key      = None
running_total = 0
chan_found = False
chan_found_last = False
desired_channel = 'ABC'

# loop through output from mapper
# - sequential operation dependent on the mappers' output
for input_line in sys.stdin:
    input_line = input_line.strip()
    #mylog.write(input_line+"\n")

    input_line.split("\t", 1)
    this_key, value = input_line.split("\t") # split at tab, Hadoop default

    if last_key != this_key: # main trigger occurs when key value changes
        chan_found_last = (True if chan_found else False)
        chan_found = False
    if value == desired_channel:
        chan_found = True
        
    # catches when channel is in the value field
    try:
        value_int = int(value)
    except:
        value_int = 0

    if last_key == this_key:
        running_total += value_int
    else: #(last_key != this_key):
        if chan_found_last:
            print( "{0}\t{1}".format(last_key, running_total) )
        running_total = value_int
        last_key = this_key

if (last_key == this_key) & chan_found: # deal with last line
    print( "{0}\t{1}".format(last_key, running_total)) 

#mylog.close()
