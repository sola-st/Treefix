import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

def frame_or_series(data): return pd.Series(data) # pragma: no cover
def indexer_sli(obj): return obj.iloc # pragma: no cover
pd.array = lambda data, dtype: pd.Series(data, dtype=dtype).to_numpy() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_na_indexing.py
# https://github.com/pandas-dev/pandas/issues/31503
from l3.Runtime import _l_
obj = frame_or_series([1, 2, 3])
_l_(4463)

mask = pd.array([True, False, None], dtype="boolean")
_l_(4464)

result = indexer_sli(obj)[mask]
_l_(4465)
expected = indexer_sli(obj)[mask.fillna(False)]
_l_(4466)

tm.assert_equal(result, expected)
_l_(4467)
