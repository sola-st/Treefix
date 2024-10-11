class MockBase: # pragma: no cover
    def check_opname(self, s, op_name, other, exc=None): # pragma: no cover
        print('check_opname executed') # pragma: no cover

class DerivedClass(MockBase): # pragma: no cover
    def super_check_opname(self): # pragma: no cover
        return super().check_opname # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
