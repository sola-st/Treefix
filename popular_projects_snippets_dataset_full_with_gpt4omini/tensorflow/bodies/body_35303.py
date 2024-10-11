# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
pdf = np.zeros_like(x) + 1.0 / (b_v - a_v)
pdf[x > b_v] = 0.0
pdf[x < a_v] = 0.0
pdf[5] = 1.0 / (20.0 - 15.0)
exit(pdf)
