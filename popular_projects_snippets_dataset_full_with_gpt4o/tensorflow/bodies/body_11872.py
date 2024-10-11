# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_permutation.py
"""Static check of perm."""
if (perm.shape.ndims is not None and perm.shape.ndims < 1):
    raise ValueError(f"Argument `perm` must have at least 1 dimension. "
                     f"Received: {perm}.")
if not perm.dtype.is_integer:
    raise TypeError(f"Argument `perm` must be integer dtype. "
                    f"Received: {perm}.")
# Check that the permutation satisfies the uniqueness constraint.
static_perm = tensor_util.constant_value(perm)
if static_perm is not None:
    sorted_perm = np.sort(static_perm, axis=-1)
    if np.any(sorted_perm != np.arange(0, static_perm.shape[-1])):
        raise ValueError(
            f"Argument `perm` must be a vector of unique integers from "
            f"0 to {static_perm.shape[-1] - 1}.")
