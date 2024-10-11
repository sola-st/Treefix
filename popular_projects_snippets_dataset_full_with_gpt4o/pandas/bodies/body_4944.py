# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#48379
ser = Series([1, 2, 3, 4, 5], dtype="Int64")
ser_numpy_dtype = Series([1, 2, 3, 4, 5], dtype="int64")
result = ser.var(ddof=ddof)
result_numpy_dtype = ser_numpy_dtype.var(ddof=ddof)
assert result == result_numpy_dtype
assert result == exp
