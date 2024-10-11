# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
func = lambda: nn_ops.conv2d(m1, m2, strides=[1, 1, 1, 1], padding="VALID")
self._run(func, num_iters)
