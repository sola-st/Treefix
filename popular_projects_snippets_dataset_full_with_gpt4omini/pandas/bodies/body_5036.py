# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_arithmetic.py
# https://github.com/pandas-dev/pandas/issues/32023
result = getattr(interval, method)(delta)
left = getattr(interval.left, method)(delta)
right = getattr(interval.right, method)(delta)
expected = Interval(left, right)

assert result == expected
