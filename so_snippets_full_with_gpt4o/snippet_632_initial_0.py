 # pragma: no cover

class SomeClass:# pragma: no cover
    def __init__(self, param1):# pragma: no cover
        self.param1 = param1 # pragma: no cover
_param1_value = 42 # pragma: no cover
self = type("Mock", (object,), {"assertTrue": lambda x, y: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises
from l3.Runtime import _l_
p = SomeClass(param1=_param1_value)
_l_(12051)
self.assertTrue(isinstance(p, SomeClass))
_l_(12052)

