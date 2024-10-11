# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable()
self.assertIsInstance(v.handle, ops.Tensor)
self.assertEqual(v.handle.dtype, dtypes.resource)
