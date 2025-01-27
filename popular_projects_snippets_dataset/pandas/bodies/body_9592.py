# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_arithmetic.py
# https://github.com/pandas-dev/pandas/issues/22022
# https://github.com/pandas-dev/pandas/issues/29997
arr = pd.array([np.nan, np.nan], dtype="Float64")
result = np.array([1.0, 2.0]) ** arr
expected = pd.array([1.0, np.nan], dtype="Float64")
tm.assert_extension_array_equal(result, expected)
