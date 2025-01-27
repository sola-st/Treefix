# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
func = lambda: constant_op.constant([3.0])[0]
self._run(func, 30000)
