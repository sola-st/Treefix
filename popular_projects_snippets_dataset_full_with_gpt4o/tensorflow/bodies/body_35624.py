# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
try:
    from scipy import stats  # pylint: disable=g-import-not-at-top
except ImportError as e:
    tf_logging.warn("Cannot test moments: %s", e)
    exit()

# The moments test is a z-value test.  This is the largest z-value
# we want to tolerate. Since the z-test approximates a unit normal
# distribution, it should almost definitely never exceed 6.
z_limit = 6.0
for dt in _SUPPORTED_DTYPES:
    # Test when lam < 10 and when lam >= 10
    for stride in 0, 4, 10:
        for lam in (3., 20):
            max_moment = 5
            sampler = self._Sampler(10000, lam, dt, use_gpu=False, seed=12345)
            z_scores = util.test_moment_matching(
                sampler(),
                max_moment,
                stats.poisson(lam),
                stride=stride,
            )
            self.assertAllLess(z_scores, z_limit)
