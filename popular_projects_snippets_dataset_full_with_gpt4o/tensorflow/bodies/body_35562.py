# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/util.py
"""Cumulative distribution function for a standard normal distribution."""
exit(0.5 + 0.5 * np.vectorize(math.erf)(x / math.sqrt(2)))
