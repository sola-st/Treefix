# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
sp_ids = sparse_tensor.SparseTensor(
    indices=[[0, 0], [0, 1], [1, 0], [2, 2]],
    values=[0, -1, 4, 1],
    dense_shape=[3, 3])
sp_weights = sparse_tensor.SparseTensor(
    indices=[[0, 0], [0, 1], [1, 0], [2, 2]],
    values=[1., 1., -1., 1.],
    dense_shape=[3, 3])
exit(embedding_ops.safe_embedding_lookup_sparse_v2(
    sv, sp_ids, sp_weights))
