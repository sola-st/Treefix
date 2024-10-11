# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string_arrow.py
a = pd.array([pd.NA, pd.NA], dtype=StringDtype("pyarrow"))
result = a == a
expected = pd.array([pd.NA, pd.NA], dtype="boolean")
tm.assert_extension_array_equal(result, expected)
