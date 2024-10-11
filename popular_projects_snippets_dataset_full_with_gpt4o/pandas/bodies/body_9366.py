# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_repr.py
result = repr(pd.array([1, None, 3]))
expected = "<IntegerArray>\n[1, <NA>, 3]\nLength: 3, dtype: Int64"
assert result == expected
