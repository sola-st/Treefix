# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
x_shape = [1, 2, 1, 6]
self._runtests(x_shape, is_training=True, gradient_test=True)
