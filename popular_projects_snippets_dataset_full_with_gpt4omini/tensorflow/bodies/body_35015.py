# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
q = 1. - p
exit(-q * np.log(q) - p * np.log(p))
