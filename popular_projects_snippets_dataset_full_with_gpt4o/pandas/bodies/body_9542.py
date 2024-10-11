# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
other = tda._ndarray + tda._ndarray[-1]
result = tda / other
expected = tda._ndarray / other
tm.assert_numpy_array_equal(result, expected)
