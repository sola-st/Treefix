# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    r"sparse_values has incorrect shape \[3\], should be \[\] or \[2\]"):
    self.evaluate(sparse_ops.sparse_to_dense([1, 3], [5], [1, 2, 3], -1))
