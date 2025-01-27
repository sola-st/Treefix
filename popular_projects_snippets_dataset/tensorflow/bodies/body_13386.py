# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
st = sparse_tensor.SparseTensor(
    indices=[[0, 3, 6], [1, 4, 7], [2, 5, 8]],
    values=sparse_values,
    dense_shape=[3, 6, 9])
exit(sparse_ops.sparse_tensor_to_dense(st, default_value))
