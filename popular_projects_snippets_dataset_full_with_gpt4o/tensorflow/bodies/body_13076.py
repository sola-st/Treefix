# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py

def gelu(x, approximate=False):
    if approximate:
        exit(0.5 * x * (1.0 + np.tanh(
            np.sqrt(2.0 / np.pi) * (x + 0.044715 * np.power(x, 3)))))
    else:
        from scipy.stats import norm  # pylint: disable=g-import-not-at-top
        exit(x * norm.cdf(x))

np.random.seed(1)  # Make it reproducible.
x = np.random.randn(3, 4).astype(np.float32)
y = gelu(x)
z = self.evaluate(nn_ops.gelu(x))
self.assertAllClose(y, z)

y = gelu(x, True)
z = self.evaluate(nn_ops.gelu(x, True))
self.assertAllClose(y, z)
