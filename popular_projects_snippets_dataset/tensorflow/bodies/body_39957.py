# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
xs = [[[np.linspace(0, 1, 21).tolist()] * 20] * 20]
self._run(lambda: constant_op.constant(xs, dtype=dtypes.float64), 10000)
