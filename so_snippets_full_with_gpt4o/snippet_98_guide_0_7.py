import sys # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
from l3.Runtime import _l_
print >> sys.stderr, 'spam' 
_l_(14584) 

print("spam", file=sys.stderr) 
_l_(14585) 

