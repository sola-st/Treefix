arr = [] # pragma: no cover
arr.append('HI') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not
from l3.Runtime import _l_
arr = []
_l_(2527)
arr.append["HI"]
_l_(2528)

