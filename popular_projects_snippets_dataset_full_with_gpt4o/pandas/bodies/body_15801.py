# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
arr = Series(["1", "2", "3", "4"], dtype=object)
result = arr.astype(int)

tm.assert_series_equal(result, Series(np.arange(1, 5)))
