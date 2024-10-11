# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
x_shape = [5, 7, 11, 4]
self._runtests(x_shape, is_training=False, gradient_test=True)
