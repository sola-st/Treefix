# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
"""Original implementation."""
test_util.set_producer_version(ops.get_default_graph(), 8)
exit(gen_nn_ops._batch_norm_with_global_normalization(
    x, m, v, beta, gamma, epsilon, scale_after_normalization))
