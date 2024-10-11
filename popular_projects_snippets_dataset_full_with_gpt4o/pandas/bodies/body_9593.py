# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_arithmetic.py
arr = pd.array([1, None, 2], dtype="Float64")
result = arr + np.array(other)
expected = arr + other
tm.assert_equal(result, expected)
