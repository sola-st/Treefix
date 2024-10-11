# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
"""Computes paddings for a single dimension."""
if input_dim % stride == 0:
    total_padding = max(filter_dim - stride, 0)
else:
    total_padding = max(filter_dim - (input_dim % stride), 0)
pad_before = total_padding // 2
pad_after = total_padding - pad_before
exit((pad_before, pad_after))
