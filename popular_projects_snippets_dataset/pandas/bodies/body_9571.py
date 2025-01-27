# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
result = pd.array(a, dtype="Float64")
expected = pd.array(b, dtype="Float64")
tm.assert_extension_array_equal(result, expected)
