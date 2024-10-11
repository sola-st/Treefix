import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas.core.arrays import StringArray # pragma: no cover
import pandas.testing as tm # pragma: no cover

string_storage = 'arrow' # pragma: no cover
val = 'c' # pragma: no cover
NA = None # pragma: no cover
_maybe_upcast = lambda arr, use_nullable_dtypes: arr # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_upcast.py
# GH#36712
from l3.Runtime import _l_
try:
    import pyarrow as pa
    _l_(9731)

except ImportError:
    pass

with pd.option_context("mode.string_storage", string_storage):
    _l_(9740)

    arr = np.array(["a", "b", val], dtype=np.object_)
    _l_(9732)
    result = _maybe_upcast(arr, use_nullable_dtypes=True)
    _l_(9733)

    if string_storage == "python":
        _l_(9738)

        exp_val = "c" if val == "c" else NA
        _l_(9734)
        expected = StringArray(np.array(["a", "b", exp_val], dtype=np.object_))
        _l_(9735)
    else:
        exp_val = "c" if val == "c" else None
        _l_(9736)
        expected = ArrowStringArray(pa.array(["a", "b", exp_val]))
        _l_(9737)
    tm.assert_extension_array_equal(result, expected)
    _l_(9739)
