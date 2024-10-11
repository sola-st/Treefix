import sys # pragma: no cover

import sys # pragma: no cover

class MockStream:# pragma: no cover
    def write(self, msg): pass# pragma: no cover
    def flush(self): pass # pragma: no cover
sys.stderr = MockStream() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
from l3.Runtime import _l_
print >> sys.stderr, 'spam' 
_l_(2276) 

print("spam", file=sys.stderr) 
_l_(2277) 

