# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
with self.session(use_gpu=use_gpu, graph=ops.Graph()) as sess:
    if graph_seed is not None:
        random_seed.set_random_seed(graph_seed)
    x = rng_func([num], min_or_mean, max_or_stddev, dtype=dtype, seed=op_seed)

    y = self.evaluate(x)
    z = self.evaluate(x)
    w = self.evaluate(x)

    # We use exact equality here. If the random-number generator is producing
    # the same output, all three outputs will be bitwise identical.
    self.assertTrue((not np.array_equal(y, z)) or
                    (not np.array_equal(z, w)) or (not np.array_equal(y, w)))
