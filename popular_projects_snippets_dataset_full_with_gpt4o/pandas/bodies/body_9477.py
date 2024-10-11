# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
# The logical operations should not assume that masked values are False!
a = pd.arrays.BooleanArray(
    np.array([True, True, True, False, False, False, True, False, True]),
    np.array([False] * 6 + [True, True, True]),
)
b = pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype="boolean")
if isinstance(other, list):
    other = pd.array(other, dtype="boolean")

result = getattr(a, all_logical_operators)(other)
expected = getattr(b, all_logical_operators)(other)
tm.assert_extension_array_equal(result, expected)

if isinstance(other, BooleanArray):
    other._data[other._mask] = True
    a._data[a._mask] = False

    result = getattr(a, all_logical_operators)(other)
    expected = getattr(b, all_logical_operators)(other)
    tm.assert_extension_array_equal(result, expected)
