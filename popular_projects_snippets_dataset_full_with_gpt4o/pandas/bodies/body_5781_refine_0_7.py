import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover
import numpy as np # pragma: no cover

data_for_grouping = np.array([True, False, True], dtype=np.bool_) # pragma: no cover
pa_dtype = pa.bool_() # pragma: no cover
pa.types = type('Mock', (object,), {'is_boolean': lambda x: x == pa.bool_()}) # pragma: no cover
request = type('Mock', (object,), {'node': type('Mock', (object,), {'add_marker': lambda self, x: None})()}) # pragma: no cover

import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover
import numpy as np # pragma: no cover

class MockDtype: # pragma: no cover
    pyarrow_dtype = pa.bool_() # pragma: no cover
 # pragma: no cover
data_for_grouping = type('Mock', (object,), {'dtype': MockDtype()}) # pragma: no cover
pa.types = type('Mock', (object,), {'is_boolean': lambda x: x == pa.bool_()}) # pragma: no cover
request = type('Mock', (object,), {'node': type('Mock', (object,), {'add_marker': lambda self, x: None})()}) # pragma: no cover

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
