# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
# Each row demonstrates a test case:
#   Row 0: multiple valid ids, 1 invalid id, weighted mean
#   Row 1: all ids are invalid (leaving no valid ids after pruning)
#   Row 2: no ids to begin with
#   Row 3: single id
#   Row 4: all ids have <=0 weight
indices = [[0, 0], [0, 1], [0, 2], [1, 0], [3, 0], [4, 0], [4, 1]]
ids = [0, 1, -1, -1, 2, 0, 1]
weights = [1.0, 2.0, 1.0, 1.0, 3.0, 0.0, -0.5]
shape = [5, 4]

sparse_ids = sparse_tensor.SparseTensor(
    constant_op.constant(indices, dtypes.int64),
    constant_op.constant(ids, dtypes.int64),
    constant_op.constant(shape, dtypes.int64))

sparse_weights = sparse_tensor.SparseTensor(
    constant_op.constant(indices, dtypes.int64),
    constant_op.constant(weights, dtypes.float32),
    constant_op.constant(shape, dtypes.int64))

exit((sparse_ids, sparse_weights))
