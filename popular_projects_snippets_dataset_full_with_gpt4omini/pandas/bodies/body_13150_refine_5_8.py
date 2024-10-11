import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pyarrow.parquet as pq # pragma: no cover
import numpy as np # pragma: no cover
from contextlib import contextmanager # pragma: no cover
import warnings # pragma: no cover

df_cross_compat = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12]}) # pragma: no cover
tm = type('Mock', (object,), {'ensure_clean': staticmethod(lambda: contextmanager(lambda: (yield 'mock_path'))()), 'assert_frame_equal': staticmethod(lambda left, right: None)})() # pragma: no cover
fp = 'pyarrow' # pragma: no cover
catch_warnings = warnings.catch_warnings # pragma: no cover
read_parquet = pq.read_table # pragma: no cover

import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pyarrow.parquet as pq # pragma: no cover
import numpy as np # pragma: no cover
import tempfile # pragma: no cover
from warnings import catch_warnings # pragma: no cover

df_cross_compat = pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6], 'd': [7, 8]}) # pragma: no cover
fp = 'pyarrow' # pragma: no cover
class MockTM:  # pragma: no cover
    @staticmethod # pragma: no cover
    def ensure_clean(): # pragma: no cover
        return tempfile.NamedTemporaryFile(delete=True).name # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_frame_equal(df1, df2): # pragma: no cover
        pd.testing.assert_frame_equal(df1, df2) # pragma: no cover
tm = MockTM() # pragma: no cover
catch_warnings = catch_warnings # pragma: no cover
read_parquet = lambda path: pd.read_parquet(path) # pragma: no cover
pa = pa # pragma: no cover

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
