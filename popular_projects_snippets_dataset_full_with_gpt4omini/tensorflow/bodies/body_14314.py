# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/public_symbol_test.py
a = 0.1
b = 0.2
self.assertAllClose(onp.add(a, b), np.add(a, b))
