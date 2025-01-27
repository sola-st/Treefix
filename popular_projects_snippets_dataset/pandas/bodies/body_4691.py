# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# GH 10155
# In the previous implementation mean can overflow for int dtypes, it
# is now consistent with numpy

ser = Series(val, index=range(500), dtype=np.int64)
result = ser.mean()
np_result = ser.values.mean()
assert result == val
assert result == np_result
assert result.dtype == np.float64
