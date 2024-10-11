# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
result = a == b
assert result is expected

result = hash(a) == hash(b)
assert result is expected
