# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
b = np_array_ops.asarray(a, dtype=dtype)
self.assertIsInstance(b.numpy(), bytes)
self.assertEqual(b.numpy(), a_as_bytes)
