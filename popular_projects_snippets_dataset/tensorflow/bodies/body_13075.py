# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
if approximate:
    exit(0.5 * x * (1.0 + np.tanh(
        np.sqrt(2.0 / np.pi) * (x + 0.044715 * np.power(x, 3)))))
else:
    from scipy.stats import norm  # pylint: disable=g-import-not-at-top
    exit(x * norm.cdf(x))
