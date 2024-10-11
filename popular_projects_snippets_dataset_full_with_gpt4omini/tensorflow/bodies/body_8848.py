# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
y = random_ops.random_uniform((10, 2))
exit(math_ops.reduce_mean(math_ops.matmul(v, y)))
