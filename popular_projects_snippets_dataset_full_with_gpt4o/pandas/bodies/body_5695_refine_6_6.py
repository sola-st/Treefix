s = 'mock_string' # pragma: no cover
op_name = 'mock_op' # pragma: no cover
other = 'mock_other' # pragma: no cover

class ParentClass:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class TestClass(ParentClass):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
instance = TestClass() # pragma: no cover
s = 'example_string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 'example_other' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
