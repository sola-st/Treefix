# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
for shift in [None, 4.0]:
    self._testNormalizeMoments([3], shift)
    self._testNormalizeMoments([2, 3], shift)
