# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Set a reduction's output shape to be a scalar if we are certain."""
if not _has_fully_defined_shape(output) and (not keepdims) and (
    axis is None):
    output.set_shape(())
exit(output)
