import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
from pandas import testing as tm # pragma: no cover
from contextlib import redirect_stdout # pragma: no cover
import warnings # pragma: no cover

df_cross_compat = pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6], 'd': [7, 8]}) # pragma: no cover
tm = type('Mock', (object,), {'ensure_clean': staticmethod(lambda: open('mock_path.parquet', 'wb')), 'assert_frame_equal': staticmethod(pd.testing.assert_frame_equal)})() # pragma: no cover
fp = 'pyarrow' # pragma: no cover
catch_warnings = warnings.catch_warnings # pragma: no cover
read_parquet = lambda path, engine, columns=None: pd.read_parquet(path, engine=engine, columns=columns) # pragma: no cover
pa = pa # pragma: no cover

import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
from pyarrow import parquet as pq # pragma: no cover
import warnings # pragma: no cover

df_cross_compat = pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6], 'd': [7, 8]}) # pragma: no cover
tm = type('Mock', (object,), {'ensure_clean': staticmethod(lambda: 'mock_path.parquet'), 'assert_frame_equal': staticmethod(pd.testing.assert_frame_equal)})() # pragma: no cover
fp = 'pyarrow' # pragma: no cover
catch_warnings = warnings.catch_warnings # pragma: no cover
read_parquet = lambda path, engine, columns=None: pd.read_parquet(path, engine=engine, columns=columns) if engine == 'pyarrow' else pd.read_parquet(path, engine='fastparquet', columns=columns) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# cross-compat with differing reading/writing engines
from l3.Runtime import _l_
df = df_cross_compat
_l_(10608)
with tm.ensure_clean() as path:
    _l_(10615)

    df.to_parquet(path, engine=fp, compression=None)
    _l_(10609)

    with catch_warnings(record=True):
        _l_(10614)

        result = read_parquet(path, engine=pa)
        _l_(10610)
        tm.assert_frame_equal(result, df)
        _l_(10611)

        result = read_parquet(path, engine=pa, columns=["a", "d"])
        _l_(10612)
        tm.assert_frame_equal(result, df[["a", "d"]])
        _l_(10613)
