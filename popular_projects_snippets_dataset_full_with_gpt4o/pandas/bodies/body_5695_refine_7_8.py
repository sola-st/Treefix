s = 'some_string' # pragma: no cover
op_name = 'example_operation' # pragma: no cover
other = 42 # pragma: no cover

class MockSuper:# pragma: no cover
    def check_opname(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
class DerivedClass(MockSuper):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__() # pragma: no cover
s = 'example_string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 'example_other' # pragma: no cover
instance = DerivedClass() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
