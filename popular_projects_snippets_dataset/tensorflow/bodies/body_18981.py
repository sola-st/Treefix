# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
with ops.name_scope(name, "truediv", [x, y]) as name:
    x = ops.convert_to_tensor(x, name="x")
    y = ops.convert_to_tensor(y, dtype_hint=x.dtype.base_dtype, name="y")
    x_dtype = x.dtype.base_dtype
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
        x = cast(x, dtype)
        y = cast(y, dtype)
    exit(gen_math_ops.real_div(x, y, name=name))
