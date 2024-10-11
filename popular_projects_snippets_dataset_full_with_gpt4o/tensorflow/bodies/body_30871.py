# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    x, _, _ = _EmbeddingParams(1, 10, dtype=dtypes.float32)
    sp_ids = sparse_tensor.SparseTensor(
        constant_op.constant([[0, 0], [0, 1], [1, 0]], dtypes.int64),
        constant_op.constant([0, 1, 2], dtypes.int32),
        constant_op.constant([2, 2], dtypes.int64))
    sp_weights = sparse_tensor.SparseTensor(
        constant_op.constant([[0, 0], [0, 1]], dtypes.int64),
        constant_op.constant([12.0, 5.0], dtypes.float32),
        constant_op.constant([1, 2], dtypes.int64))

    with self.assertRaises(ValueError):
        embedding_ops.embedding_lookup_sparse(
            x, sp_ids, sp_weights, combiner="mean")
