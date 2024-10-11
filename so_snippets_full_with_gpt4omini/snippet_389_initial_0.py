from typing import List # pragma: no cover

sequence = [1, 2, 3, 4, 5] # pragma: no cover
def process(item): print(item) # pragma: no cover
suite = 'All items processed successfully' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
from l3.Runtime import _l_
for item in sequence:
    _l_(970)

    process(item)
    _l_(968)
else:  # no break
    suite
    _l_(969)

