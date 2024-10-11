# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
try:
    from scipy import stats  # pylint: disable=g-import-not-at-top
except ImportError as e:
    tf_logging.warn("Cannot test moments: %s", e)
    exit()
# The moments test is a z-value test.  This is the largest z-value
# we want to tolerate. Since the z-test approximates a unit normal
# distribution, it should almost definitely never exceed 6.
z_limit = 6.0
gen = stateful_random_ops.Generator.from_seed(seed=12345)
for dt in _SUPPORTED_DTYPES:
    # Test when n * p > 10, and n * p < 10
    for stride in 0, 4, 10:
        for counts in (1., 10., 22., 50.):
            for prob in (0.1, 0.5, 0.8):
                sampler = self._Sampler(int(5e4), counts, prob, dt, gen=gen)
                z_scores = util.test_moment_matching(
                    # Use float64 samples.
                    self.evaluate(sampler()).astype(np.float64),
                    number_moments=6,
                    dist=stats.binom(counts, prob),
                    stride=stride,
                )
                self.assertAllLess(z_scores, z_limit)
