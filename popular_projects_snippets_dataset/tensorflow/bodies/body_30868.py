# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
vocab_size = 13
batch_size = 10
param_shape = [2, 5]
expected_lookup_result_shape = [None] + param_shape

sp_ids, sp_weights, ids, weights, vals_per_batch_entry = (
    self._RandomIdsAndWeights(batch_size, vocab_size))

grouped_ids = self._GroupByBatchEntry(ids, vals_per_batch_entry)
grouped_weights = self._GroupByBatchEntry(weights, vals_per_batch_entry)
grouped_ignored_weights = self._GroupByBatchEntry(
    np.ones(np.sum(vals_per_batch_entry)), vals_per_batch_entry)

for num_shards, combiner, dtype, ignore_weights in itertools.product(
    [1, 5], ["sum", "mean", "sqrtn"],
    [dtypes.float16, dtypes.bfloat16, dtypes.float32, dtypes.float64],
    [True, False]):

    with self.cached_session():
        p, params, feed_dict = _EmbeddingParams(
            num_shards, vocab_size, shape=param_shape, dtype=dtype)
        embedding_sum = embedding_ops.embedding_lookup_sparse(
            p,
            sp_ids,
            None if ignore_weights else sp_weights,
            combiner=combiner)

        self.assertEqual(embedding_sum.get_shape().as_list(),
                         expected_lookup_result_shape)
        self.assertEqual(embedding_sum.dtype, dtype)

        tf_embedding_sum = embedding_sum.eval(feed_dict=feed_dict)

        np_embedding_sum, np_weight_sum, np_weight_sq_sum = _EmbeddingResult(
            params,
            grouped_ids,
            num_shards,
            vocab_size,
            weight_vals=grouped_ignored_weights
            if ignore_weights else grouped_weights)
        if combiner == "mean":
            np_embedding_sum /= np.reshape(np_weight_sum, (batch_size, 1, 1))
        if combiner == "sqrtn":
            np_embedding_sum /= np.reshape(
                np.sqrt(np_weight_sq_sum), (batch_size, 1, 1))

        rtol = 1e-6
        if dtype == dtypes.bfloat16:
            rtol = 1e-2
        elif dtype == dtypes.float16:
            rtol = 1e-3
        atol = rtol
        self.assertAllClose(np_embedding_sum, tf_embedding_sum, rtol, atol)
