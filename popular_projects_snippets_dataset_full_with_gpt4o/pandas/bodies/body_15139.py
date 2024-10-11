# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
index = lexsorted_two_level_string_multiindex
ser = Series(range(len(index)), index=index, name="sth")
expected = [
    "first  second",
    "foo    one       0",
    "       two       1",
    "       three     2",
    "bar    one       3",
    "       two       4",
    "baz    two       5",
    "       three     6",
    "qux    one       7",
    "       two       8",
    "       three     9",
    "Name: sth, dtype: int64",
]
expected = "\n".join(expected)
assert repr(ser) == expected
