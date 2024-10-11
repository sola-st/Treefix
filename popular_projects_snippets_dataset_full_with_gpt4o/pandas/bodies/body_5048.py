# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
# GH27219
# non-empty always return False
iv = Interval(left, right, closed)
assert iv.is_empty is False

# same endpoint is empty except when closed='both' (contains one point)
iv = Interval(left, left, closed)
result = iv.is_empty
expected = closed != "both"
assert result is expected
