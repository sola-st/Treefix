# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
"""Static check of diag."""
if diag.shape.ndims is not None and diag.shape.ndims < 1:
    raise ValueError("Argument diag must have at least 1 dimension.  "
                     "Found: %s" % diag)
