# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session() as sess:
    num_shards = 2
    vocab_size = 4
    p, p_variable, params, feed_dict = _EmbeddingParamsAsPartitionedVariable(
        num_shards, vocab_size)

    id_vals = np.array([0, 0])
    ids = constant_op.constant(list(id_vals), dtype=dtypes.int32)
    print("Construct ids", ids.get_shape())
    embedding = embedding_ops.embedding_lookup(p_variable, ids)
    self.evaluate(variables.global_variables_initializer())
    params_values = [params[p_i.name] for p_i in p]
    # Test that the PartitionedVariable components equal the list in p
    p_var_val = self.evaluate(list(p_variable))
    # Actual test
    tf_result = embedding.eval(feed_dict=feed_dict)
np_result, _, _ = _EmbeddingResult(params, id_vals, num_shards, vocab_size)
self.assertAllEqual(params_values, p_var_val)
self.assertAllEqual(np_result, tf_result)
self.assertShapeEqual(np_result, embedding)
