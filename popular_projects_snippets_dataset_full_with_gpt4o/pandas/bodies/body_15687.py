# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_diff.py
# int dtype
a = 10000000000000000
b = a + 1
ser = Series([a, b])

result = ser.diff()
assert result[1] == 1
