# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# int dtype
a = 10_000_000_000_000_000
b = a + 1
ser = Series([a, b])

rs = DataFrame({"s": ser}).diff()
assert rs.s[1] == 1
