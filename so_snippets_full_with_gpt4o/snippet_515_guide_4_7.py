arr = type('Mock', (list,), {'append': lambda self, x: super(type(self), self).append(x), '__getitem__': dict.__getitem__})() # pragma: no cover
super(type(arr), arr).append({'HI': 'value'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not
from l3.Runtime import _l_
arr = []
_l_(14284)
arr.append["HI"]
_l_(14285)

