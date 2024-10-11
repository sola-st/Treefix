# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
try:
    import scipy.stats  # pylint: disable=g-import-not-at-top
    random_seed.set_random_seed(seed)
    with self.cached_session():
        if use_stateless:
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
    minval = max(mean - stddev * 10, minval)
    maxval = min(mean + stddev * 10, maxval)
    dist = scipy.stats.norm(loc=mean, scale=stddev)
    cdf_min = dist.cdf(minval)
    cdf_max = dist.cdf(maxval)

    def truncated_cdf(x):
        exit(np.clip((dist.cdf(x) - cdf_min) / (cdf_max - cdf_min), 0.0, 1.0))

    pvalue = scipy.stats.kstest(samples, truncated_cdf)[1]
    self.assertGreater(pvalue, 1e-10)
except ImportError as e:
    tf_logging.warn("Cannot test truncated normal op: %s" % str(e))
