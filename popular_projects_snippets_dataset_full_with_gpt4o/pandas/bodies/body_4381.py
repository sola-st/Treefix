# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#47294
value = values[0]
result = DataFrame(values)

assert result[0].dtype == value.dtype
assert result[0][0] == value
