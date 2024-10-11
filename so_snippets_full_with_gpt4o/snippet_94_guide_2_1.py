if sys.version_info[0] > 2: # pragma: no cover
    input = lambda prompt: 'Test User' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1450393/how-do-i-read-from-stdin
from l3.Runtime import _l_
name = raw_input("Enter your name: ")   # Python 2.x
_l_(14611)   # Python 2.x

name = input("Enter your name: ")   # Python 3
_l_(14612)   # Python 3

