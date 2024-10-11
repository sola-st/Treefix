# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    embedding_weights = self._random_weights()
    sparse_ids, sparse_weights = self._ids_and_weights_3d()

    embedding_lookup_result = (
        embedding_ops.safe_embedding_lookup_sparse_v2(embedding_weights,
                                                      sparse_ids,
                                                      sparse_weights))

    self.assertAllClose(embedding_lookup_result, [[
        (1.0 * embedding_weights[0][0] + 2.0 * embedding_weights[0][1]) / 3.0,
        [0] * 4, [0] * 4
    ], [embedding_weights[0][2], [0] * 4, [0] * 4]])
