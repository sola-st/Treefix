# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# Cannot cast to an unsigned integer
# because we have a negative number.
data = ["-1", 2, 3]
expected = np.array([-1, 2, 3], dtype=np.int64)

res = to_numeric(data, downcast="unsigned")
tm.assert_numpy_array_equal(res, expected)
