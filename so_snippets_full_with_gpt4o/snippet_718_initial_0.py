def func(type): # pragma: no cover
    print(f'Function called with type: {type}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5710391/converting-python-dict-to-kwargs
from l3.Runtime import _l_
func(**{'type':'Event'})
_l_(13743)

func(type='Event')
_l_(13744)

