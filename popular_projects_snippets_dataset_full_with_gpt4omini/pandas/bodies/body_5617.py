# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
s = date_range("20000101", periods=2000000, freq="s").values
result = algos.isin(s, s[0:2])
expected = np.zeros(len(s), dtype=bool)
expected[0] = True
expected[1] = True
tm.assert_numpy_array_equal(result, expected)
