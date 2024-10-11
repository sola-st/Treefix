# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_numpy.py
# https://github.com/pandas-dev/pandas/issues/35455
df = DataFrame([[Timestamp("2020-01-01 00:00:00"), 100.0]])
result = df.to_numpy(dtype=str)
expected = np.array([["2020-01-01 00:00:00", "100.0"]], dtype=str)
tm.assert_numpy_array_equal(result, expected)
