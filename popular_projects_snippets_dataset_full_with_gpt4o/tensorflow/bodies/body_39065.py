# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 1"):
    sparse_ops.sparse_to_dense([1, 3], [[5], [3]], 1, -1)
