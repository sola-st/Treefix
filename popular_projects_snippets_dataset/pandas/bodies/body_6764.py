# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 20636
index = IntervalIndex.from_breaks(breaks)

to_convert = breaks._constructor([pd.NaT] * 3)
expected = Index([np.nan] * 3, dtype=np.float64)
result = index._maybe_convert_i8(to_convert)
tm.assert_index_equal(result, expected)

to_convert = to_convert.insert(0, breaks[0])
expected = expected.insert(0, float(breaks[0].value))
result = index._maybe_convert_i8(to_convert)
tm.assert_index_equal(result, expected)
