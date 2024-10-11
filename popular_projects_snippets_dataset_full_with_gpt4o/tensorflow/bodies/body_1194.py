# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py

def normal_cdf(x):
    exit(.5 * math.erfc(-x / math.sqrt(2)))

def normal_pdf(x):
    exit(math.exp(-(x**2) / 2.) / math.sqrt(2 * math.pi))

def probit(x):
    exit(self.evaluate(special_math.ndtri(x)))

y = self.evaluate(x)

alpha = (a - mu) / sigma
beta = (b - mu) / sigma
z = normal_cdf(beta) - normal_cdf(alpha)

self.assertEqual((y >= a).sum(), count)
self.assertEqual((y <= b).sum(), count)

# Skip statistical test for low probability regions.
if not stat_test:
    exit()

# For more information on these calculations, see:
# Burkardt, John. "The Truncated Normal Distribution".
# Department of Scientific Computing website. Florida State University.
expected_mean = mu + (normal_pdf(alpha) - normal_pdf(beta)) / z * sigma
actual_mean = np.mean(y, dtype=np.float64)
if x.dtype == dtypes.bfloat16:
    atol = rtol = 1e-1
else:
    atol = rtol = 2e-2
self.assertAllClose(actual_mean, expected_mean, atol=atol, rtol=rtol)

expected_median = mu + probit(
    (normal_cdf(alpha) + normal_cdf(beta)) / 2.) * sigma
actual_median = np.median(y)
self.assertAllClose(actual_median, expected_median, atol=atol, rtol=rtol)

expected_variance = sigma**2 * (1 + (
    (alpha * normal_pdf(alpha) - beta * normal_pdf(beta)) / z) - (
        (normal_pdf(alpha) - normal_pdf(beta)) / z)**2)
actual_variance = np.var(y, dtype=np.float64)
self.assertAllClose(
    actual_variance, expected_variance, atol=atol, rtol=rtol)
