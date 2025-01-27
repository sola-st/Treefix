# Extracted from ./data/repos/pandas/pandas/tests/series/test_unary.py
dtype = float_ea_dtype
ser = Series([1.1, 2.2, 3.3], dtype=dtype)
result = getattr(ser, op)()
target = result.copy(deep=True)
ser[0] = None
tm.assert_series_equal(result, target)
