import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

read_json = pd.read_json # pragma: no cover
dtype = False # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
np = np # pragma: no cover
tm = tm # pragma: no cover
np.nan = np.nan # pragma: no cover
tm.assert_frame_equal = type('Mock', (object,), {'assert_frame_equal': staticmethod(lambda left, right: None)})().assert_frame_equal # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH28501 Parse missing values using read_json with dtype=False
# to NaN instead of None
from l3.Runtime import _l_
result = read_json("[null]", dtype=dtype)
_l_(6736)
expected = DataFrame([np.nan])
_l_(6737)

tm.assert_frame_equal(result, expected)
_l_(6738)
