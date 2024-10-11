# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16475384/rename-a-dictionary-key
from l3.Runtime import _l_
d = {'a': 1, 'b': 2}
_l_(11915)
v = d['b']
_l_(11916)
del d['b']
_l_(11917)
d['c'] = v
_l_(11918)

