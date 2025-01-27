# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
# Github issue, 36359
with self.test_session():
    x = array_ops.ones((4, 5))
    sp_ids = sparse_tensor.SparseTensor(
        constant_op.constant([[1, 0], [3, 0]], dtypes.int64),
        constant_op.constant([0, 2], dtypes.int32),
        constant_op.constant([4, 1], dtypes.int64))
    sp_weights = sparse_tensor.SparseTensor(
        constant_op.constant([[1, 0], [3, 0]], dtypes.int64),
        constant_op.constant([1, 1], dtypes.float32),
        constant_op.constant([4, 1], dtypes.int64))

    for combiner in ["sum", "mean", "sqrtn"]:
        embedding_sum = embedding_ops.embedding_lookup_sparse(
            x, sp_ids, sp_weights, combiner=combiner)

        tf_embedding_sum = ops.convert_to_tensor(embedding_sum)
        self.assertAllClose(tf_embedding_sum[0], np.zeros(5))
        self.assertAllClose(tf_embedding_sum[1], np.ones(5))
        self.assertAllClose(tf_embedding_sum[2], np.zeros(5))
        self.assertAllClose(tf_embedding_sum[3], np.ones(5))
