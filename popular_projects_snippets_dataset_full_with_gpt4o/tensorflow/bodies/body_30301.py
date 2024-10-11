# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/identity_op_py_test.py
value = self.evaluate(array_ops.identity([1, 2, 3, 4, 5, 6]))
self.assertAllEqual(np.array([1, 2, 3, 4, 5, 6]), value)
