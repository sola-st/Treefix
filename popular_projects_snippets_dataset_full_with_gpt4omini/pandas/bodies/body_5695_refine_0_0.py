from typing import Any # pragma: no cover

s = 'sample_string' # pragma: no cover
op_name = 'sample_operation' # pragma: no cover
other = 'another_sample' # pragma: no cover

from typing import Any # pragma: no cover

class MockSuper:                               # Creates a mock class with a check_opname method # pragma: no cover
    def check_opname(self, s: str, op_name: str, other: Any, exc: Any = None): # pragma: no cover
        pass                                   # Placeholder for the method implementation # pragma: no cover
class Mock(MockSuper):                         # Creates a mock class inheriting from MockSuper # pragma: no cover
    pass # pragma: no cover
s = 'sample_string' # pragma: no cover
op_name = 'sample_operation' # pragma: no cover
other = 'another_sample' # pragma: no cover
mock_instance = Mock() # pragma: no cover
super = lambda: mock_instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
# overwriting to indicate ops don't raise an error
from l3.Runtime import _l_
super().check_opname(s, op_name, other, exc=None)
_l_(10513)
