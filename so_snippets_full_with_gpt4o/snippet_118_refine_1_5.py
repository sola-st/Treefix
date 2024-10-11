import sys # pragma: no cover

import sys # pragma: no cover

# Begin initialization # pragma: no cover
class MockFile: # pragma: no cover
    def __init__(self, filename, mode): # pragma: no cover
        self.file = open(filename, mode) # pragma: no cover
    def write(self, data): # pragma: no cover
        self.file.write(data) # pragma: no cover
    def flush(self): # pragma: no cover
        self.file.flush() # pragma: no cover
 # pragma: no cover
# End initialization # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
from l3.Runtime import _l_
f = open('xyz.log', 'a', 0)
_l_(13022)

sys.stdout = open('out.log', 'a', 0)
_l_(13023)

