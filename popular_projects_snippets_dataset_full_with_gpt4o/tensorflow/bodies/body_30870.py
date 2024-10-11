# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
vocab_size = 12
batch_size = 4
param_shape = [2, 3]
sp_ids, sp_weights, _, _, _ = (self._RandomIdsAndWeights(
    batch_size, vocab_size))

for num_shards, combiner, dtype, ignore_weights in itertools.product(
    [1, 3], ["sum", "mean", "sqrtn"], [dtypes.float32,
                                       dtypes.float64], [True, False]):
    with self.cached_session():
        x, params, _ = _EmbeddingParams(
            num_shards, vocab_size, shape=param_shape, dtype=dtype)

        y = embedding_ops.embedding_lookup_sparse(
            x,
            sp_ids,
            None if ignore_weights else sp_weights,
            combiner=combiner)
        x_name = [_PName(i) for i in range(num_shards)]
        x_init_value = [params[x_n + ":0"] for x_n in x_name]
        x_shape = [i.shape for i in x_init_value]
        y_shape = [batch_size] + list(params[_PName(0) + ":0"].shape[1:])
        err = gradient_checker.compute_gradient_error(
            x, x_shape, y, y_shape, x_init_value=x_init_value)
    self.assertLess(err, 1e-5 if dtype == dtypes.float64 else 2e-3)
