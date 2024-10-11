s = 'mock_string' # pragma: no cover
op_name = 'mock_op' # pragma: no cover
other = 'mock_other' # pragma: no cover

class MockParent:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class Mock(MockParent):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
mock_instance = Mock() # pragma: no cover
s = 'example_string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 'example_other' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
