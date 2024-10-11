s = 'sample_string' # pragma: no cover
op_name = 'sample_op' # pragma: no cover
other = 42 # pragma: no cover

class MockSuperClass:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        print(f'Checking opname: s={s}, op_name={op_name}, other={other}, exc={exc}')# pragma: no cover
# pragma: no cover
class ExampleClass(MockSuperClass):# pragma: no cover
    def method(self):# pragma: no cover
        super().check_opname(s, op_name, other, exc=None) # pragma: no cover
s = 'example_string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 'example_other' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
