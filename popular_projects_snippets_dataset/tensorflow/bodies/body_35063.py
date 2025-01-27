# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
if not isinstance(x, np.ndarray):
    x = np.array(x)
exit(np.transpose(x, np.roll(np.arange(len(x.shape)), shift)))
