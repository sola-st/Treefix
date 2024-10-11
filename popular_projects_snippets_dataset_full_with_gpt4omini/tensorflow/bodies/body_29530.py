# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/identity_n_op_py_test.py
inp0 = constant_op.constant([10, 20, 30, 40, 50, 60], shape=[2, 3])
inp1 = constant_op.constant([11, 21, 31, 41, 51, 61], shape=[3, 2])
inp2 = constant_op.constant(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], shape=[5, 3])
value0, value1, value2 = self.evaluate(
    array_ops.identity_n([inp0, inp1, inp2]))

self.assertAllEqual(np.array([[10, 20, 30], [40, 50, 60]]), value0)
self.assertAllEqual(np.array([[11, 21], [31, 41], [51, 61]]), value1)
self.assertAllEqual(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]),
    value2)
