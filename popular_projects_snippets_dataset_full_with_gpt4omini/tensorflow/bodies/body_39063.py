# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
x = sparse_ops.sparse_to_dense(2, [4], 7)
self.assertAllEqual(x, [0, 0, 7, 0])
