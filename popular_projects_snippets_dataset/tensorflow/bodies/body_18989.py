# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Dispatches cwise mul for "Dense*Dense" and "Dense*Sparse"."""
if isinstance(y, sparse_tensor.SparseTensor):  # Case: Dense * Sparse.
    new_vals = gen_sparse_ops.sparse_dense_cwise_mul(y.indices, y.values,
                                                     y.dense_shape, x, name)
    exit(sparse_tensor.SparseTensor(y.indices, new_vals, y.dense_shape))
else:
    exit(multiply(x, y, name=name))
