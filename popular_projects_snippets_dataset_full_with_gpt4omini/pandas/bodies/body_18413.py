# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
box = index_or_series
lhs, rhs = pair
if reverse:
    # add lhs / rhs switched data
    lhs, rhs = rhs, lhs

left = Series(lhs, dtype=dtype)
right = box(rhs, dtype=dtype)

result = op(left, right)

tm.assert_series_equal(result, expected)
