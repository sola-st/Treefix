# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
b = bool(ops.convert_to_tensor(value=10))
self.assertIsInstance(b, bool)
self.assertTrue(b)
self.assertFalse(bool(ops.convert_to_tensor(value=0)))
self.assertTrue(bool(ops.convert_to_tensor(value=0.1)))
self.assertFalse(bool(ops.convert_to_tensor(value=0.0)))
