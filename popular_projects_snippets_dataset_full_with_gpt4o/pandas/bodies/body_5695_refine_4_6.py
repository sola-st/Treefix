s = 'example_string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 'example_other' # pragma: no cover

class BaseClass:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        print(f'check_opname called with {s}, {op_name}, {other}, {exc}') # pragma: no cover
class SubClass(BaseClass):# pragma: no cover
    def test_method(self, s, op_name, other):# pragma: no cover
        super().check_opname(s, op_name, other, exc=None) # pragma: no cover
instance = SubClass() # pragma: no cover
s = 'example_string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 'example_other' # pragma: no cover
instance.test_method(s, op_name, other) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
