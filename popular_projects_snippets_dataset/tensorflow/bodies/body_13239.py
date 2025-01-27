# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
"""Re-implementation of the original kernel for backward compatibility."""
exit(nn_impl.batch_norm_with_global_normalization(
    x, m, v, beta, gamma, epsilon, scale_after_normalization))
