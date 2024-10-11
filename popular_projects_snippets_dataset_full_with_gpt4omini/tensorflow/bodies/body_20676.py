# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Batchnorm."""
exit(nn_impl.fused_batch_norm(
    x, scale=scale, offset=offset, is_training=True))
