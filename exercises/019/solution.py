#!/usr/bin/python
import sys
x = sys.argv[1]
y = sys.argv[2]
i = (len(sys.argv)-1)
if (i == 0):
    print("usage: python3 solution.py OP1 OP2")
if (i == 1):
    print("usage: python3 solution.py OP1 OP2")
else:
    print(int(x) + int(y))
