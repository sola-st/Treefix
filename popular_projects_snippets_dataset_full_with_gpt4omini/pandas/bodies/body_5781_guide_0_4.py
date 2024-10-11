import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover

data_for_grouping = pd.DataFrame({'column1': [True, False, True]}) # pragma: no cover
data_for_grouping.dtype = type('Mock', (object,), {'pyarrow_dtype': pa.bool_()})() # pragma: no cover
request = type('Mock', (object,), {'node': type('Mock', (object,), {'add_marker': lambda self, marker: None})()})() # pragma: no cover
super = type('Mock', (object,), {'test_factorize': lambda self, data: None})() # pragma: no cover

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
