# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
# Since beta does not exist when scale_after_normalization=False, we only
# test for scale_after_normalization=True.
for scale_after_normalization in [True, False]:
    for v in [1, 2]:
        self._testBatchNormGradient(3, "beta", scale_after_normalization, True,
                                    v)
