# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
n = samples.size
np.random.seed(137)
if not stats:
    exit()
sample_scipy = stats.t.rvs(df, loc=mu, scale=sigma, size=n)
covg = 0.99
r = stats.t.interval(covg, df, loc=mu, scale=sigma)
bins = 100
hist, _ = np.histogram(samples, bins=bins, range=r)
hist_scipy, _ = np.histogram(sample_scipy, bins=bins, range=r)
self.assertGreater(hist.sum(), n * (covg - .01))
self.assertGreater(hist_scipy.sum(), n * (covg - .01))
hist_min1 = hist + 1.  # put at least one item in each bucket
hist_norm = hist_min1 / hist_min1.sum()
hist_scipy_min1 = hist_scipy + 1.  # put at least one item in each bucket
hist_scipy_norm = hist_scipy_min1 / hist_scipy_min1.sum()
kl_appx = np.sum(np.log(hist_scipy_norm / hist_norm) * hist_scipy_norm)
self.assertLess(kl_appx, 1)
