# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
"""Static check of reflection_axis."""
if (reflection_axis.shape.ndims is not None and
    reflection_axis.shape.ndims < 1):
    raise ValueError(
        "Argument reflection_axis must have at least 1 dimension.  "
        "Found: %s" % reflection_axis)
