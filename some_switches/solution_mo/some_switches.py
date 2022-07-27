#!/usr/bin/env python3

# python3 ./some_switches.py

# https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python
# https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file-in-python-3

import sys


door_cnt=10
pass_cnt=10
show_hist=False
outLoc = sys.stdout


if len(sys.argv) >= 2 : door_cnt=int(sys.argv[1])
if len(sys.argv) >= 3 : pass_cnt=int(sys.argv[2])
if len(sys.argv) >= 4 and len(sys.argv[3]) : show_hist=True
if len(sys.argv) >= 5 and len(sys.argv[4]) : outLoc = open(sys.argv[4], "a")

switches = [False] * door_cnt

for i in range(pass_cnt):
    for j in range(i, door_cnt, i+1):
        switches[j] = not switches[j]
    if show_hist :
        for j in range( door_cnt):
            print('_ ' if switches[j] else 'X ', end="", file=outLoc)
        print("", file=outLoc)

for i in range(door_cnt):
    print("Switch %d is" % (i+1), 'open.' if switches[i] else 'close.', file=outLoc)

outLoc.close()