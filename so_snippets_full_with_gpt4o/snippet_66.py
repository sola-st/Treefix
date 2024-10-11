# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
from l3.Runtime import _l_
a = ['a', 'b', 'c', 'd']
_l_(12543)
a.pop(1)
_l_(12544)

# now a is ['a', 'c', 'd']

a = ['a', 'b', 'c', 'd']
_l_(12545)
a.pop()
_l_(12546)

# now a is ['a', 'b', 'c']

