import sys # pragma: no cover

sys = type('MockSys', (object,), {'stdout': None})() # pragma: no cover
sys.stdout = open('mock_out.log', 'a') # pragma: no cover

import sys # pragma: no cover

sys = type('Mock', (object,), {})() # pragma: no cover
sys.stdout = open('mock_out.log', 'a') # pragma: no cover
f = open('xyz.log', 'a') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
from l3.Runtime import _l_
f = open('xyz.log', 'a', 0)
_l_(1376)

sys.stdout = open('out.log', 'a', 0)
_l_(1377)

