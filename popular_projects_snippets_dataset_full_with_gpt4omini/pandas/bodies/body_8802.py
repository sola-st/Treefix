# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
expected = pd.arrays.StringArray(np.array(["a", pd.NA]))
tm.assert_extension_array_equal(
    pd.arrays.StringArray(np.array(["a", na], dtype="object")), expected
)
