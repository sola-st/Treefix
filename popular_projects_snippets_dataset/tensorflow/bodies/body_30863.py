# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
np.random.seed(8)
with self.cached_session():
    for params_shape in (12,), (6, 3), (6, 2, 3):
        # Test embedding rank 0, 1, 2.
        # Note: the first dimension must be a common multiple of procs below.
        params = 2 * np.ones(params_shape)
        params_norm = params / np.sqrt(
            np.sum(
                params * params, tuple(range(params.ndim)[1:]), keepdims=True))
        for ids_shape in (), (3), (4, 3), (2, 3, 4):
            ids = np.random.randint(
                params.shape[0], size=np.prod(ids_shape,
                                              dtype=np.int64)).reshape(ids_shape)
            # Compare nonsharded to gather
            simple = embedding_ops.embedding_lookup(params, ids, max_norm=1.0)
            # assertAllClose is used here as different implementations of sqrt may
            # be used to compute each of the values being compared.  For example,
            # on AVX512 builds the embedding operation makes use of Eigen's fast
            # vectorized square root algorithm for doubles.  These different
            # implementations of sqrt are not guaranteed to produce exactly the
            # same results. Therefore, an exact comparison cannot be made.
            self.assertAllClose(simple, array_ops.gather(params_norm, ids))
            # Run a few different sharded versions.
            for procs in 1, 2, 3:
                stride = procs * math_ops.range(params.shape[0] // procs)
                split_params = [
                    array_ops.gather(params, stride + p) for p in range(procs)
                ]
                sharded = embedding_ops.embedding_lookup(
                    split_params, ids, max_norm=1.0)
                self.assertAllEqual(simple, sharded)
