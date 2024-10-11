import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from pandas.core.arrays.string_ import StringArray # pragma: no cover
from pandas import NA # pragma: no cover
from typing import Any # pragma: no cover

string_storage = 'python' # pragma: no cover
val = 'c' # pragma: no cover
def _maybe_upcast(arr: Any, use_nullable_dtypes: bool) -> Any:# pragma: no cover
    return StringArray(arr) if use_nullable_dtypes else arr # pragma: no cover
class Mock:# pragma: no cover
    @staticmethod# pragma: no cover
    def assert_extension_array_equal(result: Any, expected: Any):# pragma: no cover
        assert result.equals(expected), f"{result} != {expected}" # pragma: no cover
tm = Mock # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_upcast.py
# GH#36712
from l3.Runtime import _l_
try:
    import pyarrow as pa
    _l_(20613)

except ImportError:
    pass

with pd.option_context("mode.string_storage", string_storage):
    _l_(20622)

    arr = np.array(["a", "b", val], dtype=np.object_)
    _l_(20614)
    result = _maybe_upcast(arr, use_nullable_dtypes=True)
    _l_(20615)

    if string_storage == "python":
        _l_(20620)

        exp_val = "c" if val == "c" else NA
        _l_(20616)
        expected = StringArray(np.array(["a", "b", exp_val], dtype=np.object_))
        _l_(20617)
    else:
        exp_val = "c" if val == "c" else None
        _l_(20618)
        expected = ArrowStringArray(pa.array(["a", "b", exp_val]))
        _l_(20619)
    tm.assert_extension_array_equal(result, expected)
    _l_(20621)
