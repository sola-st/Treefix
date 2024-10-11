# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# invalid dates can be help as object
result = Series([datetime(2, 1, 1)])
assert result[0] == datetime(2, 1, 1, 0, 0)

result = Series([datetime(3000, 1, 1)])
assert result[0] == datetime(3000, 1, 1, 0, 0)
