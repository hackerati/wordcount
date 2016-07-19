#!/usr/bin/env python3

import sys

def read_input (file):
    for line in file:
        # split the line into words
        yield line.split ()

def main (separator='\t'):
    # input comes from STDIN (standard input)
    lines = read_input (sys.stdin)

    for line in lines:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        [print (word + separator + '1') for word in line]

if __name__ == "__main__":
    main ()
