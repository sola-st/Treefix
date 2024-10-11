# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
y = array_ops.reshape(
    math_ops.matmul(x, kernel), []) - constant_op.constant(1.)
exit(y * y)
