# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
"""New implementation."""
exit(nn_impl.batch_normalization(x, m, v, beta if
                                   shift_after_normalization else None,
                                   gamma if scale_after_normalization else
                                   None, epsilon))
