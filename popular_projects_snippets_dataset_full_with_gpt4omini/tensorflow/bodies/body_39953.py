# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
xs = [[0] * 2] * 40
self._run(lambda: constant_op.constant(xs), 1000)
