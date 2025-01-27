# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    num_shards = 2
    vocab_size = 4
    p, params, feed_dict = _EmbeddingParams(num_shards, vocab_size)

    id_vals = np.array([0, 0])
    ids = constant_op.constant(list(id_vals), dtype=dtypes.int32)
    print("Construct ids", ids.get_shape())
    embedding = embedding_ops.embedding_lookup(p, ids)

    tf_result = embedding.eval(feed_dict=feed_dict)
np_result, _, _ = _EmbeddingResult(params, id_vals, num_shards, vocab_size)
self.assertAllEqual(np_result, tf_result)
self.assertShapeEqual(np_result, embedding)
