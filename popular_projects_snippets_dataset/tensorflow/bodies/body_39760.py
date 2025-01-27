# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
func = lambda: math_ops.multiply(m, m)
self._run(func, num_iters)
