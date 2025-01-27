# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    embedding_weights = self._random_weights(num_shards=3)
    sparse_ids, sparse_weights = self._ids_and_weights_2d()

    embedding_weights[1] = embedding_weights[1].astype(np.float64)
    self.assertRaises(TypeError, embedding_ops.safe_embedding_lookup_sparse,
                      embedding_weights, sparse_ids)
    embedding_weights = [
        constant_op.constant(w, dtype=dtypes.float64)
        for w in embedding_weights
    ]
    self.assertRaises(ValueError, embedding_ops.safe_embedding_lookup_sparse,
                      embedding_weights, sparse_ids, sparse_weights)
