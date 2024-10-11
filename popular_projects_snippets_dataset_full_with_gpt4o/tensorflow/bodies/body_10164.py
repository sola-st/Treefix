# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
values = np.random.uniform(0.1, 1.9, size=int(1e4)).astype(np.float32)
approx_id = math_ops.erfc(math_ops.erfcinv(values))
self.assertAllClose(values, self.evaluate(approx_id))
