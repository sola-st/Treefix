# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
values = constant_op.constant(
    0.554979503, shape=[5], dtype=dtypes.float32)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 1"):
    indices = constant_op.constant(0, shape=[5, 2], dtype=dtypes.int64)
    dense_shape = constant_op.constant(53, shape=[], dtype=dtypes.int64)
    csr = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
        indices=indices, values=values, dense_shape=dense_shape)
    self.evaluate(csr)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 2"):
    indices = constant_op.constant(0, shape=[5], dtype=dtypes.int64)
    dense_shape = constant_op.constant(53, shape=[1], dtype=dtypes.int64)
    csr = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
        indices=indices, values=values, dense_shape=dense_shape)
    self.evaluate(csr)
