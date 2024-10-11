# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
self.assertAllEqual(0, np_array_ops.ndim(0.5))
self.assertAllEqual(1, np_array_ops.ndim([1, 2]))
