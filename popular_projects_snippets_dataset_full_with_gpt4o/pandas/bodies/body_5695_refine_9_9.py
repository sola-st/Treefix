s = 'example_string' # pragma: no cover
op_name = 'example_op_name' # pragma: no cover
other = 'example_other' # pragma: no cover

class MockSuperClass:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        print(f"check_opname called with s={s}, op_name={op_name}, other={other}, exc={exc}")# pragma: no cover
# pragma: no cover
class DerivedClass(MockSuperClass):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
instance = DerivedClass() # pragma: no cover
s = 'example_string' # pragma: no cover
op_name = 'example_op_name' # pragma: no cover
other = 'example_other' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
