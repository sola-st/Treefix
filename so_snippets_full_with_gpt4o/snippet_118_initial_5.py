import sys # pragma: no cover

type('Mock', (object,), {'stdout': None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
from l3.Runtime import _l_
f = open('xyz.log', 'a', 0)
_l_(13022)

sys.stdout = open('out.log', 'a', 0)
_l_(13023)

