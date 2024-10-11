# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
a = pd.array([True, False, None], dtype="boolean")
result = a & other
expected = pd.array(expected, dtype="boolean")
tm.assert_extension_array_equal(result, expected)

result = other & a
tm.assert_extension_array_equal(result, expected)

# ensure we haven't mutated anything inplace
tm.assert_extension_array_equal(
    a, pd.array([True, False, None], dtype="boolean")
)
