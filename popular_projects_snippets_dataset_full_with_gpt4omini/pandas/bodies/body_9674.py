# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_constructors.py
result = period_array(data, freq=freq).asi8
expected = np.asarray(expected, dtype=np.int64)
tm.assert_numpy_array_equal(result, expected)
