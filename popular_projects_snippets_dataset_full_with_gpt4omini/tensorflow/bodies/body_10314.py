# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
x_shape = [1, 1, 1, 1]
# GPU kernel doesn't properly handle case where non-channel dimensions are 1
self._runtests(x_shape, is_training=False, gradient_test=True,
               cpu_only=True)
