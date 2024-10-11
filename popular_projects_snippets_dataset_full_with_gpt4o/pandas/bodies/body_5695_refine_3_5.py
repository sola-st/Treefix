s = 'example string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 42 # pragma: no cover

class MockBaseClass:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        print(f"Checked: {s}, {op_name}, {other}, {exc}") # pragma: no cover
class DerivedClass(MockBaseClass):# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        super().check_opname(s, op_name, other, exc) # pragma: no cover
s = 'some_string' # pragma: no cover
op_name = 'operation_name' # pragma: no cover
other = 'other_value' # pragma: no cover
instance = DerivedClass() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
