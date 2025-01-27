# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_mask.py
# GH#50488
ser = Series([0.0, 1.0, 2.0, 3.0], dtype=Float64Dtype())
cond = ~ser.isna()
other = Series([True, False, True, False])
excepted = Series([1.0, 0.0, 1.0, 0.0], dtype=ser.dtype)
result = ser.mask(cond, other)
tm.assert_series_equal(result, excepted)
