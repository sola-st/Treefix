# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# If we can't successfully cast the given
# data to a numeric dtype, do not bother
# with the downcast parameter.
data = ["foo", 2, 3]
expected = np.array(data, dtype=object)

res = to_numeric(data, errors="ignore", downcast="unsigned")
tm.assert_numpy_array_equal(res, expected)
