# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py

# truediv
td = Timedelta("1 days 2 hours 3 ns")
result = td / np.timedelta64(1, "D")
assert result == td.value / (86400 * 10**9)
result = td / np.timedelta64(1, "s")
assert result == td.value / 10**9
result = td / np.timedelta64(1, "ns")
assert result == td.value

# floordiv
td = Timedelta("1 days 2 hours 3 ns")
result = td // np.timedelta64(1, "D")
assert result == 1
result = td // np.timedelta64(1, "s")
assert result == 93600
result = td // np.timedelta64(1, "ns")
assert result == td.value
