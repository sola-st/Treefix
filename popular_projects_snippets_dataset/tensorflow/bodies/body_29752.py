# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    self.assertRaises(ValueError, array_ops.expand_dims,
                      np.zeros([2, 3, 5]), -5)
    self.assertRaises(ValueError, array_ops.expand_dims,
                      [False, True, True], -5)
    self.assertRaises(ValueError, array_ops.expand_dims,
                      np.zeros([2, 3, 5]), 4)
    self.assertRaises(ValueError, array_ops.expand_dims,
                      [False, True, True], 4)
