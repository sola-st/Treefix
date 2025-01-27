# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
result = pd.array(a, dtype="Int64")
expected = pd.array(b, dtype="Int64")
tm.assert_extension_array_equal(result, expected)
