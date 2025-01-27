# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
try:
    from scipy import stats  # pylint: disable=g-import-not-at-top
except ImportError as e:
    tf_logging.warn("Cannot test moments: %s" % e)
    exit()

# The moments test is a z-value test.  This is the largest z-value
# we want to tolerate. Since the z-test approximates a unit normal
# distribution, it should almost definitely never exceed 6.
z_limit = 6.0

for stride in 0, 1, 4, 17:
    alphas = [0.2, 1.0, 3.0]
    if dt == dtypes.float64:
        alphas = [0.01] + alphas
    for alpha in alphas:
        for scale in 9, 17:
            # Gamma moments only defined for values less than the scale param.
            max_moment = min(6, scale // 2)
            sampler = self._Sampler(20000, alpha, 1 / scale, dt, seed=12345)
            z_scores = util.test_moment_matching(
                sampler(),
                max_moment,
                stats.gamma(alpha, scale=scale),
                stride=stride,
            )
            self.assertAllLess(z_scores, z_limit)
