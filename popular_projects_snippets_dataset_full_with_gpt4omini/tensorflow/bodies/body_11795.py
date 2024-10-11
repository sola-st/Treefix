# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_lower_triangular.py
"""Static check of the `tril` argument."""

if tril.shape.ndims is not None and tril.shape.ndims < 2:
    raise ValueError(
        "Argument tril must have at least 2 dimensions.  Found: %s"
        % tril)
