# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
x = random_ops.random_uniform((2, 10))
y = random_ops.random_uniform((10, 2))
check_ops.assert_non_positive_v2(
    math_ops.reduce_sum(math_ops.matmul(x, y)))
exit(x)
