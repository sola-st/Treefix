# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
sparse = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=values, dense_shape=[3, 4])
sparse = sparse_ops.sparse_reshape(sparse, shape=(12,))
exit(sparse.values)
