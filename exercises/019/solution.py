#!/usr/bin/python
import sys
x = sys.argv[1]
y = sys.argv[2]
if (int(x) + int(y)):
    print(int(x) + int(y))
else:
    print("usage: python3 solution.py OP1 OP2")
