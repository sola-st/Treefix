# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
func = lambda idx=constant_op.constant(0): constant_op.constant([3.0])[idx]
self._run(func, 30000)
