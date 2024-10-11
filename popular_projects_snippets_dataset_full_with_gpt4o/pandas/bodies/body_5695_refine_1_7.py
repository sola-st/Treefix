s = 'some_string' # pragma: no cover
op_name = 'an_operation_name' # pragma: no cover
other = 'another_value' # pragma: no cover

class MockSuperClass:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        pass # pragma: no cover
class MockClass(MockSuperClass):# pragma: no cover
    pass # pragma: no cover
s = 'some_string' # pragma: no cover
op_name = 'an_operation_name' # pragma: no cover
other = 'another_value' # pragma: no cover
self_instance = MockClass() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
