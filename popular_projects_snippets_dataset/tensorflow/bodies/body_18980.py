# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Internal helper function for 'sp_t / dense_t'."""
with ops.name_scope(name, "truediv",
                    [sp_indices, sp_values, sp_shape, y]) as name:
    sp_values = ops.convert_to_tensor(sp_values, name="sp_values")
    y = ops.convert_to_tensor(y, name="y")
    x_dtype = sp_values.dtype.base_dtype
    y_dtype = y.dtype.base_dtype
    if x_dtype != y_dtype:
        raise TypeError(f"`x` and `y` must have the same dtype, "
                        f"got {x_dtype!r} != {y_dtype!r}.")
    try:
        dtype = _TRUEDIV_TABLE[x_dtype]
    except KeyError:
        raise TypeError(
            f"Invalid dtype {x_dtype!r} in __truediv__. Expected one "
            f"of {{{', '.join([repr(x) for x in _TRUEDIV_TABLE.keys()])}}}.")
    if dtype is not None:
        sp_values = cast(sp_values, dtype)
        y = cast(y, dtype)
    exit(gen_sparse_ops.sparse_dense_cwise_div(
        sp_indices, sp_values, sp_shape, y, name=name))
