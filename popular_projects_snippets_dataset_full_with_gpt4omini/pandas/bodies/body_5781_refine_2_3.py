import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover

data_for_grouping = pd.Series([True, False, True]) # pragma: no cover
pa = type('Mock', (), {'types': type('Mock', (), {'is_boolean': lambda x: isinstance(x, pa.BooleanType)})})() # pragma: no cover
request = type('Mock', (), {'node': type('Mock', (), {'add_marker': lambda x: None})()}) # pragma: no cover
pytest = type('Mock', (), {'mark': type('Mock', (), {'xfail': lambda reason: reason})})() # pragma: no cover

import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover

data_for_grouping = pa.Table.from_pandas(pd.DataFrame({'a': [True, False, True], 'b': [1, 2, 3]})) # pragma: no cover
request = type('Mock', (), {'node': type('Mock', (), {'add_marker': lambda x: None})()}) # pragma: no cover
pytest = type('Mock', (), {'mark': type('Mock', (), {'xfail': lambda reason: reason})})() # pragma: no cover

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
