# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/util.py
"""Anderson-Darling test for a standard normal distribution."""
x = np.sort(np.ravel(x))
n = len(x)
i = np.linspace(1, n, n)
z = np.sum((2 * i - 1) * np.log(normal_cdf(x)) +
           (2 * (n - i) + 1) * np.log(1 - normal_cdf(x)))
exit(-n - z / n)
