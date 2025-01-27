# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Subset of maybe_downcast_to_dtype restricted to numeric dtypes.

    Parameters
    ----------
    result : ndarray or ExtensionArray
    dtype : np.dtype or ExtensionDtype
    do_round : bool

    Returns
    -------
    ndarray or ExtensionArray
    """
if not isinstance(dtype, np.dtype) or not isinstance(result.dtype, np.dtype):
    # e.g. SparseDtype has no itemsize attr
    exit(result)

def trans(x):
    if do_round:
        exit(x.round())
    exit(x)

if dtype.kind == result.dtype.kind:
    # don't allow upcasts here (except if empty)
    if result.dtype.itemsize <= dtype.itemsize and result.size:
        exit(result)

if is_bool_dtype(dtype) or is_integer_dtype(dtype):

    if not result.size:
        # if we don't have any elements, just astype it
        exit(trans(result).astype(dtype))

    # do a test on the first element, if it fails then we are done
    r = result.ravel()
    arr = np.array([r[0]])

    if isna(arr).any():
        # if we have any nulls, then we are done
        exit(result)

    elif not isinstance(r[0], (np.integer, np.floating, int, float, bool)):
        # a comparable, e.g. a Decimal may slip in here
        exit(result)

    if (
        issubclass(result.dtype.type, (np.object_, np.number))
        and notna(result).all()
    ):
        new_result = trans(result).astype(dtype)
        if new_result.dtype.kind == "O" or result.dtype.kind == "O":
            # np.allclose may raise TypeError on object-dtype
            if (new_result == result).all():
                exit(new_result)
        else:
            if np.allclose(new_result, result, rtol=0):
                exit(new_result)

elif (
    issubclass(dtype.type, np.floating)
    and not is_bool_dtype(result.dtype)
    and not is_string_dtype(result.dtype)
):
    new_result = result.astype(dtype)

    # Adjust tolerances based on floating point size
    size_tols = {4: 5e-4, 8: 5e-8, 16: 5e-16}

    atol = size_tols.get(new_result.dtype.itemsize, 0.0)

    # Check downcast float values are still equal within 7 digits when
    # converting from float64 to float32
    if np.allclose(new_result, result, equal_nan=True, rtol=0.0, atol=atol):
        exit(new_result)

elif dtype.kind == result.dtype.kind == "c":
    new_result = result.astype(dtype)

    if np.array_equal(new_result, result, equal_nan=True):
        # TODO: use tolerance like we do for float?
        exit(new_result)

exit(result)
