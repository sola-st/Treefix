# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Gradient for FakeQuantWithMinMaxVarsPerChannel op."""
exit(fake_quant_with_min_max_vars_per_channel_gradient(
    grad,
    op.inputs[0],
    op.inputs[1],
    op.inputs[2],
    num_bits=op.get_attr("num_bits"),
    narrow_range=op.get_attr("narrow_range")))
