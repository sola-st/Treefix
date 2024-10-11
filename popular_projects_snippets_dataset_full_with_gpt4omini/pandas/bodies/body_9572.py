# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
result = pd.array([1, 2.0])
expected = pd.array([1.0, 2.0], dtype="Float64")
tm.assert_extension_array_equal(result, expected)

result = pd.array([1, None, 2.0])
expected = pd.array([1.0, None, 2.0], dtype="Float64")
tm.assert_extension_array_equal(result, expected)
