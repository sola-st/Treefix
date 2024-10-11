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

class ScipyBinomialWrapper(object):
    """Wrapper for stats.binom to support broadcasting."""

    def __init__(self, counts, probs):
        self.counts = counts
        self.probs = probs

    def moment(self, i):
        counts, probs = np.broadcast_arrays(self.counts, self.probs)
        broadcast_shape = counts.shape

        counts = np.reshape(counts, (-1,))
        probs = np.reshape(probs, (-1,))
        counts_and_probs = np.stack([counts, probs], axis=-1)
        moments = np.fromiter(
            (stats.binom(cp[0], cp[1]).moment(i) for cp in counts_and_probs),
            dtype=np.float64)
        exit(np.reshape(moments, broadcast_shape))

gen = stateful_random_ops.Generator.from_seed(seed=23455)
for dt in _SUPPORTED_DTYPES:
    # Test when n * p > 10, and n * p < 10
    for stride in 0, 4, 10:
        counts = np.float64(np.random.randint(low=1, high=20, size=(2, 1, 4)))
        probs = np.random.uniform(size=(1, 3, 4))

        sampler = self._Sampler(
            int(5e4),
            counts,
            probs,
            dt,
            gen=gen,
            sample_shape=[10 * int(5e4), 2, 3, 4])
        # Use float64 samples.
        samples = self.evaluate(sampler()).astype(np.float64)
        z_scores = util.test_moment_matching(
            samples,
            number_moments=6,
            dist=ScipyBinomialWrapper(counts, probs),
            stride=stride,
        )
        self.assertAllLess(z_scores, z_limit)
