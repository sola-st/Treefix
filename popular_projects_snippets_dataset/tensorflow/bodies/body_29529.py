# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/identity_n_op_py_test.py
value0, value1 = self.evaluate(
    array_ops.identity_n([[1, 2, 3, 4, 5, 6],
                          [b"a", b"b", b"C", b"d", b"E", b"f", b"g"]]))

self.assertAllEqual(np.array([1, 2, 3, 4, 5, 6]), value0)
self.assertAllEqual(
    np.array([b"a", b"b", b"C", b"d", b"E", b"f", b"g"]), value1)
