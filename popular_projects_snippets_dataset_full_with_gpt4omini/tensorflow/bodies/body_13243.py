# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
for scale_after_normalization in [True, False]:
    for shift_after_normalization in [True, False]:
        # shift_after_normalization=False is not supported in version 1.
        for v in ([1, 2] if shift_after_normalization else [2]):
            self._testBatchNormGradient(param_index, tag,
                                        scale_after_normalization,
                                        shift_after_normalization, v,
                                        err_tolerance)
