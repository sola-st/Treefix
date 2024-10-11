import sys # pragma: no cover

import sys # pragma: no cover

# The error occurred because unbuffered mode (0) is not allowed for text I/O.# pragma: no cover
# Changing to buffered mode by removing the third argument.# pragma: no cover
f = open('xyz.log', 'a')# pragma: no cover
# pragma: no cover
# Similarly, changing to buffered mode for stdout.# pragma: no cover
sys.stdout = open('out.log', 'a') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
from l3.Runtime import _l_
f = open('xyz.log', 'a', 0)
_l_(13022)

sys.stdout = open('out.log', 'a', 0)
_l_(13023)

