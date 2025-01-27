# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
"""Static check of row and column."""
for name, tensor in [["row", row], ["col", col]]:
    if tensor.shape.ndims is not None and tensor.shape.ndims < 1:
        raise ValueError("Argument {} must have at least 1 dimension.  "
                         "Found: {}".format(name, tensor))

if row.shape[-1] is not None and col.shape[-1] is not None:
    if row.shape[-1] != col.shape[-1]:
        raise ValueError(
            "Expected square matrix, got row and col with mismatched "
            "dimensions.")
