# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# 32-bit taking
# GH#8129
index = date_range("2000-01-01", periods=5)
arr = np.arange(5, dtype=dtype)
s1 = frame_or_series(arr, index=index)
p = arr[1]
result = s1.shift(periods=p)
expected = frame_or_series([np.nan, 0, 1, 2, 3], index=index)
tm.assert_equal(result, expected)
