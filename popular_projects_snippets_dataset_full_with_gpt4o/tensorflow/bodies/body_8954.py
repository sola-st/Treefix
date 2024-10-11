# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
x = random_ops.random_uniform((2, 10))
y = random_ops.random_uniform((10, 2))
self.iteration.assign_add(1.0)
exit(math_ops.reduce_mean(math_ops.matmul(x, y)))
