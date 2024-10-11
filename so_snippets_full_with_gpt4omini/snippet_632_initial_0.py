import unittest # pragma: no cover

class SomeClass: pass # pragma: no cover
_param1_value = 42 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises
from l3.Runtime import _l_
p = SomeClass(param1=_param1_value)
_l_(332)
self.assertTrue(isinstance(p, SomeClass))
_l_(333)

