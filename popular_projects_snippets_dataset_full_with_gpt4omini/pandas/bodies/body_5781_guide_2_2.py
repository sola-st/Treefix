import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover

class MockNode:  # Mock class for request.node # pragma: no cover
    def add_marker(self, marker): pass # pragma: no cover
class MockRequest:  # Mock class to hold MockNode # pragma: no cover
    def __init__(self): self.node = MockNode() # pragma: no cover
request = MockRequest() # pragma: no cover
data_for_grouping = pa.array([True, False, True]) # pragma: no cover
# Valid boolean data to trigger the condition # pragma: no cover
class MockSuper:  # Mock class to simulate super() behavior # pragma: no cover
    def test_factorize(self, data): print(f'Testing factorization of: {data}') # pragma: no cover
super = MockSuper() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
from l3.Runtime import _l_
pa_dtype = data_for_grouping.dtype.pyarrow_dtype
_l_(9971)
if pa.types.is_boolean(pa_dtype):
    _l_(9973)

    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"{pa_dtype} only has 2 unique possible values",
        )
    )
    _l_(9972)
super().test_factorize(data_for_grouping)
_l_(9974)
