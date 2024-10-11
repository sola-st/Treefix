# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta("1 day")
other = np.array(td.asm8)

result = td + other
assert isinstance(result, Timedelta)
assert result == 2 * td

result = other + td
assert isinstance(result, Timedelta)
assert result == 2 * td

result = other - td
assert isinstance(result, Timedelta)
assert result == 0 * td

result = td - other
assert isinstance(result, Timedelta)
assert result == 0 * td
