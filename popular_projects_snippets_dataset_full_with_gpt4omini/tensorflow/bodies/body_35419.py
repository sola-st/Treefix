# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
try:
    # TruncatedNormalMoments requires scipy.stats.
    # Give up early if we are unable to import it.
    random_seed.set_random_seed(seed)
    with self.cached_session():
        if use_stateless:
            # Generate a seed that stateless ops can use.
            new_seed = random_ops.random_uniform([2],
                                                 seed=seed,
                                                 minval=0,
                                                 maxval=(2**31 - 1),
                                                 dtype=np.int32)
            samples = stateless.stateless_parameterized_truncated_normal(
                shape, new_seed, mean, stddev, minval, maxval).eval()
        else:
            samples = random_ops.parameterized_truncated_normal(
                shape, mean, stddev, minval, maxval).eval()
        assert (~np.isnan(samples)).all()
    moments = calculate_moments(samples, self.max_moment)
    expected_moments = TruncatedNormalMoments(mean, stddev, minval, maxval)
    num_samples = functools.reduce(lambda x, y: x * y, shape, 1)
    for i in range(1, len(moments)):
        self.assertLess(
            z_test(moments, expected_moments, i, num_samples), self.z_limit)
except ImportError as e:
    tf_logging.warn("Cannot test truncated normal op: %s" % str(e))
