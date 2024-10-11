# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
vocab_size = 9
num_ids = 10
id_vals = list(np.random.randint(vocab_size, size=num_ids))
tf_logging.vlog(1, id_vals)
for ids_shape in [(10,), (2, 5)]:
    for num_shards in [1, 3]:
        with self.cached_session():
            ids = constant_op.constant(
                id_vals, shape=ids_shape, dtype=dtypes.int32)
            x, params, _ = _EmbeddingParams(num_shards, vocab_size, shape=[2])
            y = embedding_ops.embedding_lookup(x, ids)
            y_shape = ids_shape + tuple(params[_PName(0) + ":0"].shape[1:])
            x_name = [_PName(i) for i in range(num_shards)]
            x_init_value = [params[x_n + ":0"] for x_n in x_name]
            x_shape = [i.shape for i in x_init_value]
            err = gradient_checker.compute_gradient_error(
                x, x_shape, y, y_shape, x_init_value=x_init_value)
        self.assertLess(err, 1e-4)
