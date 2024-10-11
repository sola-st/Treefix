# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
cdf = (x - a_v) / (b_v - a_v)
cdf[x >= b_v] = 1
cdf[x < a_v] = 0
exit(cdf)
