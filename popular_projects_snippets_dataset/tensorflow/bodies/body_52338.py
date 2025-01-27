# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
exit(sparse_ops.sparse_add(
    input_sparse_tensor,
    sparse_tensor.SparseTensor(((0, 0), (1, 1)), (2.0, 2.0), (2, 2))
))
