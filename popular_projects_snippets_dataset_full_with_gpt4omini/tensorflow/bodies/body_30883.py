# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    embedding_weights = self._random_weights(num_shards=3)
    sparse_ids, _ = self._ids_and_weights_3d()

    embedding_lookup_result = (
        embedding_ops.safe_embedding_lookup_sparse_v2(embedding_weights,
                                                      sparse_ids, None))

    embedding_weights = list(itertools.chain(*embedding_weights))
    self.assertAllClose(embedding_lookup_result, [[
        (embedding_weights[0] + embedding_weights[1]) / 2.0, [0] * 4, [0] * 4
    ], [
        embedding_weights[2],
        (embedding_weights[0] + embedding_weights[1]) / 2.0, [0] * 4
    ]])
