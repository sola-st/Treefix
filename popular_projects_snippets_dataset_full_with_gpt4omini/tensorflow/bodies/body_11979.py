# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py
s = math_ops.sobol_sample(10, 100, dtype=dtypes.float32)
self.assertAllEqual([100, 10], self.evaluate(s).shape)
