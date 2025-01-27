# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "default_value should be a scalar"):
    self.evaluate(sparse_ops.sparse_to_dense([1, 3], [5], [1, 2], [0]))
