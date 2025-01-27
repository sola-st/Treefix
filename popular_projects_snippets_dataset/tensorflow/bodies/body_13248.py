# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
# If scale_after_normalization is False, backprop for gamma in v1
# will be 0. In version 2 of the API, if scale_after_normalization is False,
# gamma is not used at all, and the gradient is None, which displeases the
# gradient checker.
for scale_after_normalization in [True, False]:
    self._testBatchNormGradient(4, "gamma", scale_after_normalization, True,
                                1)
for shift_after_normalization in [True, False]:
    self._testBatchNormGradient(4, "gamma", True, shift_after_normalization,
                                2)
