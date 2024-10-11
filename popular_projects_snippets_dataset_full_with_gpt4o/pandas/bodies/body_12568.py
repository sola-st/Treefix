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
