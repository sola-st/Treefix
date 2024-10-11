# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
N = 1000
codes = np.arange(N)
old = Index(codes)
expected = np.arange(N - 1, -1, -1, dtype=np.int16)
new = Index(expected)
result = recode_for_categories(codes, old, new)
tm.assert_numpy_array_equal(result, expected)
