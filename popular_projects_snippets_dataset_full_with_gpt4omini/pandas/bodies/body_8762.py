# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
result = period_array(["2000", "2001", None], freq="D").asi8
expected = np.array([10957, 11323, iNaT])
tm.assert_numpy_array_equal(result, expected)
