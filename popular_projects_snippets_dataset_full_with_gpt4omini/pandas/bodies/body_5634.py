# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH#46485
ser = Series([1378774140726870442], dtype=np.uint64)
result = ser.isin([1378774140726870528])
expected = Series(False)
tm.assert_series_equal(result, expected)
