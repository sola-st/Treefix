s = 'some_string_value' # pragma: no cover
op_name = 'operation_name' # pragma: no cover
other = 'other_value' # pragma: no cover

class MockSuperClass:# pragma: no cover
    def check_opname(self, s, op_name, other, exc=None):# pragma: no cover
        print(f"check_opname called with {s}, {op_name}, {other}, exc={exc}") # pragma: no cover
class MockSubClass(MockSuperClass):# pragma: no cover
    def some_method(self):# pragma: no cover
        super().check_opname(s, op_name, other, exc=None) # pragma: no cover
s = 'some_string_value' # pragma: no cover
op_name = 'operation_name' # pragma: no cover
other = 'other_value' # pragma: no cover
# Create an instance of MockSubClass and call some_method to trigger the super() check_opname# pragma: no cover
instance = MockSubClass()# pragma: no cover
instance.some_method() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(21685)
