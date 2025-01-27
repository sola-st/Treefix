# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# see gh-14652, gh-15428
ser = Series([data] * length)
result = cut(ser, 1, labels=False)

expected = Series([0] * length, dtype=np.intp)
tm.assert_series_equal(result, expected)
