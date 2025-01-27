# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
a = pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype="boolean")
b = pd.array([True, False, None] * 3, dtype="boolean")
result = a ^ b
expected = pd.array(
    [False, True, None, True, False, None, None, None, None], dtype="boolean"
)
tm.assert_extension_array_equal(result, expected)

result = b ^ a
tm.assert_extension_array_equal(result, expected)

# ensure we haven't mutated anything inplace
tm.assert_extension_array_equal(
    a, pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype="boolean")
)
tm.assert_extension_array_equal(
    b, pd.array([True, False, None] * 3, dtype="boolean")
)
