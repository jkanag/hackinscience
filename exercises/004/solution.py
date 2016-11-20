#!/usr/bin/python
import string
tr = string.maketrans('aBCDeFGHiJKLMNoPQRSTuVWXYZ', 'AbcdEfghIjklmnOpqrstUvwxyz')
print("zyxwvutsrqponmlkjihgfedcba".translate(tr))

