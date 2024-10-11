# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_arithmetic.py
delta = klass(0)
expected = Interval(Timestamp("2020-01-01"), Timestamp("2020-02-01"))

result = delta + expected
assert result == expected

result = expected + delta
assert result == expected
