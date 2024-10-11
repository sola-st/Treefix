s = 'sample_string' # pragma: no cover
op_name = 'sample_op' # pragma: no cover
other = 42 # pragma: no cover

class Base:# pragma: no cover
    def check_opname(self, s, op_name, other, exc):# pragma: no cover
        print(f'Checking {op_name} with {s} and {other}') # pragma: no cover
class Derived(Base):# pragma: no cover
    def check_opname(self, s, op_name, other, exc):# pragma: no cover
        super().check_opname(s, op_name, other, exc) # pragma: no cover
s = 'example_string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 'example_other' # pragma: no cover
inst = Derived() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
