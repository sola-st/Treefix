# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# Swaps operands lhs and rhs. Assumes lhs is the broadcasting tensor. Due to
# ops only with right broadcastable operand like gen_math_ops.truncate_div
if (op in [gen_math_ops.truncate_div, gen_math_ops.truncate_mod]):
    exit((rhs, lhs))
exit((lhs, rhs))
