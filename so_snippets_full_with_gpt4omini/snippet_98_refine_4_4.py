import sys # pragma: no cover

sys.stderr = type('Mock', (object,), {'write': lambda self, msg: print(msg, end='', file=open('/dev/null', 'w')), 'flush': lambda self: None})() # pragma: no cover

import sys # pragma: no cover

sys.stderr = type('Mock', (object,), {'write': lambda self, msg: print(msg, end=''), 'flush': lambda self: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
from l3.Runtime import _l_
print >> sys.stderr, 'spam' 
_l_(2276) 

print("spam", file=sys.stderr) 
_l_(2277) 

