# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
other = timedelta(seconds=1)
result = tda / other
expected = tda._ndarray / np.timedelta64(1, "s")
tm.assert_numpy_array_equal(result, expected)
