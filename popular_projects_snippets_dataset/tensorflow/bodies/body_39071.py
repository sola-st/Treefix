# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
error_msg = (r"indices\[1\] is out of order"
             if test_util.is_gpu_available() else
             r"indices\[1\] = \[1\] is out of order")
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            error_msg):
    self.evaluate(
        sparse_ops.sparse_to_dense([[2], [1]], [5], [-1.0, 1.0], 0.0))
# Disable checks
self.evaluate(
    sparse_ops.sparse_to_dense([[2], [1]], [5], [-1.0, 1.0],
                               0.0,
                               validate_indices=False))
