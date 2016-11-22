#!/usr/bin/python
import string
from string import maketrans
table = maketrans('aeiou','AEIOU')
chaine =string.ascii_lowercase[::-1]
print chaine.translate(table,' ')
