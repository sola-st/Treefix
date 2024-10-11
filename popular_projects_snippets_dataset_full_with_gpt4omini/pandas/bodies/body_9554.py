# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_repr.py
result = repr(pd.array([1.0, None, 3.0]))
expected = "<FloatingArray>\n[1.0, <NA>, 3.0]\nLength: 3, dtype: Float64"
assert result == expected
