# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
r = sm_ops.csr_sparse_matrix_to_sparse_tensor(self._matrix, type=self.dtype)
exit(sparse_tensor.SparseTensor(
    indices=r.indices, values=r.values, dense_shape=r.dense_shape))
