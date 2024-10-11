# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
result = pd.array([0.1, 0.2, 0.3, 0.4])
expected = pd.array([0.1, 0.2, 0.3, 0.4], dtype="Float64")
tm.assert_extension_array_equal(result, expected)
