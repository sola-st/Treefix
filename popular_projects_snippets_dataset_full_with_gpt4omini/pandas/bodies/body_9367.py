# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_repr.py
data = pd.array([1, 2, None] * 1000)
expected = (
    "<IntegerArray>\n"
    "[   1,    2, <NA>,    1,    2, <NA>,    1,    2, <NA>,    1,\n"
    " ...\n"
    " <NA>,    1,    2, <NA>,    1,    2, <NA>,    1,    2, <NA>]\n"
    "Length: 3000, dtype: Int64"
)
result = repr(data)
assert result == expected
