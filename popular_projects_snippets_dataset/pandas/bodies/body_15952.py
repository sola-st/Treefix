# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_argsort.py
self._check_accum_op("argsort", datetime_series, check_dtype=False)
argsorted = datetime_series.argsort()
assert issubclass(argsorted.dtype.type, np.integer)

# GH#2967 (introduced bug in 0.11-dev I think)
s = Series([Timestamp(f"201301{i:02d}") for i in range(1, 6)])
assert s.dtype == "datetime64[ns]"
shifted = s.shift(-1)
assert shifted.dtype == "datetime64[ns]"
assert isna(shifted[4])

result = s.argsort()
expected = Series(range(5), dtype=np.intp)
tm.assert_series_equal(result, expected)

result = shifted.argsort()
expected = Series(list(range(4)) + [-1], dtype=np.intp)
tm.assert_series_equal(result, expected)
