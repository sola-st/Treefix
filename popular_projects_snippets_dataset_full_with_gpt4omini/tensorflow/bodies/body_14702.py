# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
v = 10
u = int(ops.convert_to_tensor(value=v))
self.assertIsInstance(u, int)
self.assertAllEqual(v, u)
