# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
minv = -2
maxv = 15
n = 100000
p = 1 / (maxv - minv)
# The counts should follow an (n, p) binomial distribution.
mean = p * n
std = np.sqrt(n * p * (1 - p))
for dt in dtypes.int32, dtypes.int64:
    # Use a fixed seed here to make the test deterministic.
    # Without the fixed seed, the 5 * std bound will (very rarely) fail.
    sampler = self._Sampler(
        n // 10, minv=minv, maxv=maxv, dtype=dt, use_gpu=True, seed=17)
    x = sampler().ravel()
    self.assertEqual(x.shape, (n,))
    counts, _ = np.histogram(x, bins=maxv - minv)
    self.assertEqual(counts.shape, (maxv - minv,))
    self.assertEqual(counts.sum(), n)
    error = np.abs(counts - mean)
    self.assertLess(error.max(), 5 * std)
