# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random_test.py
try:
    self.assertAllClose(a, b, **kwargs)
except AssertionError:
    exit()
raise AssertionError('The two values are close at all %d elements' %
                     np.size(a))
