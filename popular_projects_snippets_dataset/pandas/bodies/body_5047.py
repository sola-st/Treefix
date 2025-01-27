# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
# GH 18789
iv = Interval(Timestamp(left, tz=tz), Timestamp(right, tz=tz))
result = iv.length
expected = Timedelta(expected)
assert result == expected
