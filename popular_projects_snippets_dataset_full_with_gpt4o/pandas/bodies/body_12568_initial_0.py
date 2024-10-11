import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas._testing as tm # pragma: no cover

read_json = pd.read_json # pragma: no cover
dtype = False # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
type('Mock', (object,), {'nan': np.nan, 'assert_frame_equal': tm.assert_frame_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH28501 Parse missing values using read_json with dtype=False
# to NaN instead of None
from l3.Runtime import _l_
result = read_json("[null]", dtype=dtype)
_l_(16932)
expected = DataFrame([np.nan])
_l_(16933)

tm.assert_frame_equal(result, expected)
_l_(16934)
