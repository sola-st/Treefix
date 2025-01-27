# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
np.random.seed(8)
with self.cached_session():
    for params_shape in (12,), (6, 3):
        params = np.random.randn(*params_shape)
        for ids_shape in (3, 2), (4, 3):
            ids = np.random.randint(
                params.shape[0], size=np.prod(ids_shape)).reshape(ids_shape)
            # Compare nonsharded to gather
            simple = embedding_ops.embedding_lookup(params, ids)
            self.assertAllEqual(simple, array_ops.gather(params, ids))
            # Run a few random sharded versions
            for procs in 1, 2, 3:
                stride = procs * math_ops.range(params.shape[0] // procs)
                split_params = [
                    array_ops.gather(params, stride + p) for p in range(procs)
                ]
                sharded = embedding_ops.embedding_lookup(split_params, ids)
                self.assertAllEqual(simple, sharded)
