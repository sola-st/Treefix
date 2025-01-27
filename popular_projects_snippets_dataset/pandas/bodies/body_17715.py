# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_ticks.py
# For all Tick subclasses and all integers n, m, we should have
# tick(n) + tick(m) == tick(n+m)
# tick(n) - tick(m) == tick(n-m)
left = cls(n)
right = cls(m)
expected = cls(n + m)

assert left + right == expected

expected = cls(n - m)
assert left - right == expected
