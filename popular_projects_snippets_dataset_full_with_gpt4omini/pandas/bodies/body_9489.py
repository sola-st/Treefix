# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_construction.py
result = pd.array(a, dtype="boolean")
expected = pd.array(b, dtype="boolean")
tm.assert_extension_array_equal(result, expected)
