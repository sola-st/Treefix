# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
self.assertTrue(np.array_equal(self._Ones([2, 3]), np.array([[1] * 3] * 2)))
