# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Gradient for FakeQuantWithMinMaxArgs op."""
exit(fake_quant_with_min_max_args_gradient(
    grad,
    op.inputs[0],
    min=op.get_attr("min"),
    max=op.get_attr("max"),
    num_bits=op.get_attr("num_bits"),
    narrow_range=op.get_attr("narrow_range")))
