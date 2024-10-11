import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pyarrow.parquet as pq # pragma: no cover
import warnings # pragma: no cover
import tempfile # pragma: no cover

df_cross_compat = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'd': [7, 8, 9]}) # pragma: no cover
tm = type('Mock', (object,), {'ensure_clean': staticmethod(lambda: tempfile.NamedTemporaryFile(delete=False)), 'assert_frame_equal': staticmethod(lambda x, y: None)})() # pragma: no cover
fp = 'pyarrow' # pragma: no cover
catch_warnings = warnings.catch_warnings # pragma: no cover
read_parquet = pq.read_table # pragma: no cover

import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pyarrow.parquet as pq # pragma: no cover
import warnings # pragma: no cover
import tempfile # pragma: no cover

df_cross_compat = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'd': [7, 8, 9]}) # pragma: no cover
tm = type('Mock', (object,), {'ensure_clean': staticmethod(lambda: tempfile.NamedTemporaryFile(delete=False)), 'assert_frame_equal': staticmethod(lambda x, y: None)})() # pragma: no cover
fp = 'pyarrow' # pragma: no cover
catch_warnings = warnings.catch_warnings # pragma: no cover
def read_parquet(path, columns=None): return pq.read_table(path, columns=columns).to_pandas() # pragma: no cover

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
