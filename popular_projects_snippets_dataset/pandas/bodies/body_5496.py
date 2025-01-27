# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
# case where ndim == 0
lhs = np.datetime64(datetime(2013, 12, 6))
rhs = Timestamp("now")
nat = Timestamp("nat")

ops = {"gt": "lt", "lt": "gt", "ge": "le", "le": "ge", "eq": "eq", "ne": "ne"}

for left, right in ops.items():
    left_f = getattr(operator, left)
    right_f = getattr(operator, right)
    expected = left_f(lhs, rhs)

    result = right_f(rhs, lhs)
    assert result == expected

    expected = left_f(rhs, nat)
    result = right_f(nat, rhs)
    assert result == expected
