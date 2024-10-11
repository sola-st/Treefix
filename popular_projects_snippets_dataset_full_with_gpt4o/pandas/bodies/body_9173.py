# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
codes = np.asanyarray(codes, dtype=np.int8)
expected = np.asanyarray(expected, dtype=np.int8)
old = Index(old)
new = Index(new)
result = recode_for_categories(codes, old, new)
tm.assert_numpy_array_equal(result, expected)
