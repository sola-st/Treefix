# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
# GH 18789
iv = Interval(left, right)
result = iv.length
assert result == expected
