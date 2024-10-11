s = 'example string' # pragma: no cover
op_name = 'example_op' # pragma: no cover
other = 42 # pragma: no cover

class MockBase:# pragma: no cover
    def check_opname(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
class Mock(MockBase):# pragma: no cover
    def check_opname(self, *args, **kwargs):# pragma: no cover
        super().check_opname(*args, **kwargs) # pragma: no cover
mock_instance = Mock() # pragma: no cover
s = 'some_string' # pragma: no cover
op_name = 'some_operation' # pragma: no cover
other = 'some_other_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
