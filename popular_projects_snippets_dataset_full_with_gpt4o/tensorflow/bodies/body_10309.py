# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
x_shape = [1, 1, 6, 1]
self._runtests(x_shape, is_training=False, gradient_test=True)
