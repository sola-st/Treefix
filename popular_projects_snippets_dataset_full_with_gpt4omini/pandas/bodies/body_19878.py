# Extracted from ./data/repos/pandas/pandas/core/ops/array_ops.py
"""
    In contrast to numpy, pandas raises an error for certain operations
    with booleans.
    """
if op in _BOOL_OP_NOT_ALLOWED:
    if is_bool_dtype(a.dtype) and (
        is_bool_dtype(b) or isinstance(b, (bool, np.bool_))
    ):
        op_name = op.__name__.strip("_").lstrip("r")
        raise NotImplementedError(
            f"operator '{op_name}' not implemented for bool dtypes"
        )
