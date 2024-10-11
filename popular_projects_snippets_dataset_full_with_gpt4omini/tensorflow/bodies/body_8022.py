# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
y = array_ops.reshape(
    gen_math_ops.mat_mul(x, kernel), []) - constant_op.constant(1.)
exit(y * y)
