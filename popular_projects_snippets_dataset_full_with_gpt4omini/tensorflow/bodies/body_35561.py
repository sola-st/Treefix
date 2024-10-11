# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/util.py
"""Pearson's Chi-squared test."""
x = np.ravel(x)
n = len(x)
histogram, _ = np.histogram(x, bins=bins, range=(0, 1))
expected = n / float(bins)
exit(np.sum(np.square(histogram - expected) / expected))
