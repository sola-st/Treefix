s = 'sample_string' # pragma: no cover
op_name = 'sample_op' # pragma: no cover
other = 42 # pragma: no cover

class BaseClass:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        print(f"Checked {op_name} with {s} and {other}") # pragma: no cover
class ExampleClass(BaseClass):# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        super().check_opname(s, op_name, other, exc) # pragma: no cover
example_instance = ExampleClass() # pragma: no cover
s = 'sample_string' # pragma: no cover
op_name = 'sample_operation' # pragma: no cover
other = 'sample_other' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
