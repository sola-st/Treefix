# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_norm_benchmark.py
"""Fused kernel for batch normalization."""
# _batch_norm_with_global_normalization is deprecated in v9
test_util.set_producer_version(ops.get_default_graph(), 8)
# pylint: disable=protected-access
exit(gen_nn_ops._batch_norm_with_global_normalization(
    tensor, mean, variance, beta, gamma, 0.001, scale))
