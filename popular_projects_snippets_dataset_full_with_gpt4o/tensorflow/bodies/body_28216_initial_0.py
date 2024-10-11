import sys # pragma: no cover

counter_var = type('Mock', (object,), {'assign_add': lambda self, value: setattr(self, 'value', getattr(self, 'value', 0) + value)})() # pragma: no cover
x = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
from l3.Runtime import _l_
counter_var.assign_add(1)
_l_(20827)
aux = x
_l_(20828)
exit(aux)
