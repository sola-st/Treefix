# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
for has_shape in [True, False]:
    for keep_dims in [True, False]:
        for shift in [None, 1.0]:
            self._testSuffStats([2, 3], [1], shift, keep_dims, has_shape)
            self._testSuffStats([2, 3], [0], shift, keep_dims, has_shape)
            self._testSuffStats([1, 2, 3], [0, 2], shift, keep_dims, has_shape)
