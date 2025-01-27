# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
self.assertTrue(np_array_ops.isscalar(0.5))
self.assertTrue(np_array_ops.isscalar(5))
self.assertTrue(np_array_ops.isscalar(False))
self.assertFalse(np_array_ops.isscalar([1, 2]))
