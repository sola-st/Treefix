# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
data = [Period("2000", "D"), Period("2001", "A")]
result = Series(data)
assert result.dtype == object
assert result.tolist() == data
