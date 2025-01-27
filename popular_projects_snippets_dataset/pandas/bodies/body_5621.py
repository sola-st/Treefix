# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# https://github.com/pandas-dev/pandas/issues/22205
s = np.tile(1.0, 1_000_001)
s[0] = np.nan
result = algos.isin(s, [np.nan, 1])
expected = np.ones(len(s), dtype=bool)
tm.assert_numpy_array_equal(result, expected)
