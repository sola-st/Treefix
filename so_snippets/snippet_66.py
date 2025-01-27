# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
from l3.Runtime import _l_
a = ['a', 'b', 'c', 'd']
_l_(542)
a.pop(1)
_l_(543)

# now a is ['a', 'c', 'd']

a = ['a', 'b', 'c', 'd']
_l_(544)
a.pop()
_l_(545)

# now a is ['a', 'b', 'c']

