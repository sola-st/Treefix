# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
# This tests all combinations of:
#   - ids rank 0, 1, >1
#   - params sharded/unsharded
# It always applies max_norm.
np.random.seed(8)
l2_norm = 2.
with self.cached_session():
    # Param values are in [l2_norm, l2_norm+1) so it will always clip.
    params = np.random.rand(6, 3) + l2_norm
    params_norm = l2_norm * params / np.sqrt(
        np.sum(params * params, axis=1, keepdims=True))
    # Compute the norm of each embedding. This will change the embedding
    # rank to 0.
    params_norm = np.linalg.norm(params_norm, axis=1)
    transform = lambda x: linalg_ops.norm(x, axis=1)
    for ids_shape in (), (3), (4, 3), (2, 3, 4):
        # Test ids rank 0, 1, 2, 3.
        ids = np.random.randint(
            params.shape[0], size=np.prod(ids_shape,
                                          dtype=np.int64)).reshape(ids_shape)
        # Compare nonsharded to gather.
        simple = embedding_ops._embedding_lookup_and_transform(
            params, ids, max_norm=l2_norm, transform_fn=transform)
        self.assertAllClose(simple, array_ops.gather(params_norm, ids))
        # Run a few different sharded versions.
        for procs in 1, 2, 3:
            stride = procs * math_ops.range(params.shape[0] // procs)
            split_params = [
                array_ops.gather(params, stride + p) for p in range(procs)
            ]
            sharded = embedding_ops._embedding_lookup_and_transform(
                split_params, ids, max_norm=l2_norm, transform_fn=transform)
            # assertAllClose is used here as different implementations of sqrt may
            # be used to compute each of the values being compared.  For example,
            # on AVX512 builds the embedding operation makes use of Eigen's fast
            # vectorized square root algorithm for doubles.  These different
            # implementations of sqrt are not guaranteed to produce exactly the
            # same results. Therefore, an exact comparison cannot be made.
            self.assertAllClose(simple, sharded)
