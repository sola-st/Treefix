# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
for use_gpu in [False, True]:
    with self.cached_session(use_gpu=use_gpu):
        self.assertRaises(ValueError, array_ops.squeeze,
                          np.zeros([1, 2, 1]), [-4])
        self.assertRaises(ValueError, array_ops.squeeze,
                          np.zeros([1, 2, 1]), [0, -4])
        self.assertRaises(ValueError, array_ops.squeeze,
                          np.zeros([1, 2, 1]), [3])
        self.assertRaises(ValueError, array_ops.squeeze,
                          np.zeros([1, 2, 1]), [2, 3])
