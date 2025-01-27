# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
y = array_ops.reshape(
    math_ops.mat_mul(x, kernel), []) - array_ops.identity(1.)
exit(y * y)
