# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/identity_op_py_test.py
inp = constant_op.constant([10, 20, 30, 40, 50, 60], shape=[2, 3])
value = self.evaluate(array_ops.identity(inp))
self.assertAllEqual(np.array([[10, 20, 30], [40, 50, 60]]), value)
