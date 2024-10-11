import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover
from types import SimpleNamespace # pragma: no cover

data_for_grouping = SimpleNamespace(dtype=SimpleNamespace(pyarrow_dtype=pa.bool_())) # pragma: no cover
request = SimpleNamespace(node=SimpleNamespace(add_marker=lambda x: None)) # pragma: no cover

import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockTest:# pragma: no cover
    def test_factorize(self, data):# pragma: no cover
        pass # pragma: no cover
data_for_grouping = SimpleNamespace(dtype=SimpleNamespace(pyarrow_dtype=pa.bool_())) # pragma: no cover
request = SimpleNamespace(node=SimpleNamespace(add_marker=lambda x: None)) # pragma: no cover
super = type('MockSuper', (MockTest,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
from l3.Runtime import _l_
pa_dtype = data_for_grouping.dtype.pyarrow_dtype
_l_(21048)
if pa.types.is_boolean(pa_dtype):
    _l_(21050)

    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"{pa_dtype} only has 2 unique possible values",
        )
    )
    _l_(21049)
super().test_factorize(data_for_grouping)
_l_(21051)
