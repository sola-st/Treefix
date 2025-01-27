# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_repr.py
data = pd.array([1.0, 2.0, None] * 1000)
expected = """<FloatingArray>
[ 1.0,  2.0, <NA>,  1.0,  2.0, <NA>,  1.0,  2.0, <NA>,  1.0,
 ...
 <NA>,  1.0,  2.0, <NA>,  1.0,  2.0, <NA>,  1.0,  2.0, <NA>]
Length: 3000, dtype: Float64"""
result = repr(data)
assert result == expected
