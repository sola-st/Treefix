raw_input = input  # Mocking raw_input to act like input in Python 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1450393/how-do-i-read-from-stdin
from l3.Runtime import _l_
name = raw_input("Enter your name: ")   # Python 2.x
_l_(2335)   # Python 2.x

name = input("Enter your name: ")   # Python 3
_l_(2336)   # Python 3

