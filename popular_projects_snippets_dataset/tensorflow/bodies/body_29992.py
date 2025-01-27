# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
self.assertTrue(
    np.array_equal(self._Zeros([2, 3]), np.array([[0] * 3] * 2)))
