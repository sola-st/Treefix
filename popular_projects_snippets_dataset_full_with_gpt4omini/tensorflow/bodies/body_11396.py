# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Static assert that `tensor` has rank `2` or higher."""
sh = tensor.shape
if sh.ndims is not None and sh.ndims < 2:
    raise ValueError(
        f"Expected [batch] matrix to have at least two dimensions. Found: "
        f"{tensor}.")
