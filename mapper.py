#!/usr/bin/env python3

import sys
import re

pattern = re.compile ('[\W_]+')

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = pattern.sub (' ', line)
    # line = line.strip () # remove leading and trailing whitespace in the line
    words = line.split () # split the line into words

    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    [print (word + '\t' + '1') for word in words]
