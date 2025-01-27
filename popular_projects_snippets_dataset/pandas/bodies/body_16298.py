# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#47294
value = values[0]
result = Series(values)

assert result[0].dtype == value.dtype
assert result[0] == value
