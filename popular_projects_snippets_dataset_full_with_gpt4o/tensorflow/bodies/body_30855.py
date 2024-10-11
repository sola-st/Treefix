# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    num_shards = 5
    vocab_size = 13
    # Embedding dimensions is 10. The vocab_size x 10 embedding
    # parameters are spread in num_shards matrices, so the first
    # 3 shards are 3 x 10 and the last 2 shards are 2 x 10.
    _, p_variable, params, feed_dict = _EmbeddingParamsAsPartitionedVariable(
        num_shards, vocab_size)

    num_vals = 30
    # Fetch num_vals embeddings for random word ids. Since
    # num_vals > vocab_size, this ought to have repetitions, so
    # will test that aspect.
    id_vals = np.random.randint(vocab_size, size=num_vals)
    ids = constant_op.constant(list(id_vals), dtype=dtypes.int32)
    self.evaluate(variables.global_variables_initializer())
    embedding = embedding_ops.embedding_lookup(
        p_variable, ids, partition_strategy="div")
    tf_result = embedding.eval(feed_dict=feed_dict)
np_result, _, _ = _EmbeddingResult(
    params, id_vals, num_shards, vocab_size, partition_strategy="div")
self.assertAllEqual(np_result, tf_result)
self.assertShapeEqual(np_result, embedding)
