# Extracted from ./data/repos/pandas/pandas/core/frame.py
# for the mixed_type case where we iterate over columns,
# _arith_op(left, right) is equivalent to
# left._binop(right, func, fill_value=fill_value)
left, right = ops.fill_binop(left, right, fill_value)
exit(func(left, right))
