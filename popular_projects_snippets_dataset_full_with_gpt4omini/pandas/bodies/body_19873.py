# Extracted from ./data/repos/pandas/pandas/core/ops/array_ops.py
try:
    # For exposition, write:
    #  yarr = isinstance(y, np.ndarray)
    #  yint = is_integer(y) or (yarr and y.dtype.kind == "i")
    #  ybool = is_bool(y) or (yarr and y.dtype.kind == "b")
    #  xint = x.dtype.kind == "i"
    #  xbool = x.dtype.kind == "b"
    # Then Cases where this goes through without raising include:
    #  (xint or xbool) and (yint or bool)
    result = op(x, y)
except TypeError:
    if isinstance(y, np.ndarray):
        # bool-bool dtype operations should be OK, should not get here
        assert not (is_bool_dtype(x.dtype) and is_bool_dtype(y.dtype))
        x = ensure_object(x)
        y = ensure_object(y)
        result = libops.vec_binop(x.ravel(), y.ravel(), op)
    else:
        # let null fall thru
        assert lib.is_scalar(y)
        if not isna(y):
            y = bool(y)
        try:
            result = libops.scalar_binop(x, y, op)
        except (
            TypeError,
            ValueError,
            AttributeError,
            OverflowError,
            NotImplementedError,
        ) as err:
            typ = type(y).__name__
            raise TypeError(
                f"Cannot perform '{op.__name__}' with a dtyped [{x.dtype}] array "
                f"and scalar of type [{typ}]"
            ) from err

exit(result.reshape(x.shape))
