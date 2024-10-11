s = 'mock_string' # pragma: no cover
op_name = 'mock_op' # pragma: no cover
other = 'mock_other' # pragma: no cover

class MockSuper:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        print(f"check_opname called with: {s}, {op_name}, {other}, {exc}")# pragma: no cover
# pragma: no cover
class MockClass(MockSuper):# pragma: no cover
    def test_method(self):# pragma: no cover
        super().check_opname('sample_string', 'sample_op', 'sample_other', exc=None)# pragma: no cover
# pragma: no cover
mock_instance = MockClass()# pragma: no cover
mock_instance.test_method() # pragma: no cover
s = 'sample_string' # pragma: no cover
op_name = 'sample_op' # pragma: no cover
other = 'sample_other' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
