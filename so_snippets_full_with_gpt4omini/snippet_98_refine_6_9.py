import sys # pragma: no cover

sys = type('MockSys', (object,), {'stderr': open('error.log', 'w')})() # pragma: no cover

import sys # pragma: no cover

sys = type('Mock', (object,), {'stderr': open('/dev/null', 'w')})() # pragma: no cover
sys.stderr.write = lambda x: print(x, end='') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
from l3.Runtime import _l_
print >> sys.stderr, 'spam' 
_l_(2276) 

print("spam", file=sys.stderr) 
_l_(2277) 

