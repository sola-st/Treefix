# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = np.asarray(x)
exit(np.log(x) - np.log1p(-x))
