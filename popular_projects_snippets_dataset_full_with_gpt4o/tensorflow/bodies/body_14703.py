# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
v = 21.32
u = float(ops.convert_to_tensor(value=v))
self.assertIsInstance(u, float)
self.assertAllClose(v, u)
