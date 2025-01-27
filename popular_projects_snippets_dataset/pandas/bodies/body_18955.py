# Extracted from ./data/repos/pandas/pandas/core/construction.py
"""
    Ensure we have a 1-dimensional result array.
    """
if getattr(result, "ndim", 0) == 0:
    raise ValueError("result should be arraylike with ndim > 0")

if result.ndim == 1:
    # the result that we want
    result = _maybe_repeat(result, index)

elif result.ndim > 1:
    if isinstance(data, np.ndarray):
        if allow_2d:
            exit(result)
        raise ValueError(
            f"Data must be 1-dimensional, got ndarray of shape {data.shape} instead"
        )
    if is_object_dtype(dtype) and isinstance(dtype, ExtensionDtype):
        # i.e. PandasDtype("O")

        result = com.asarray_tuplesafe(data, dtype=np.dtype("object"))
        cls = dtype.construct_array_type()
        result = cls._from_sequence(result, dtype=dtype)
    else:
        # error: Argument "dtype" to "asarray_tuplesafe" has incompatible type
        # "Union[dtype[Any], ExtensionDtype, None]"; expected "Union[str,
        # dtype[Any], None]"
        result = com.asarray_tuplesafe(data, dtype=dtype)  # type: ignore[arg-type]
exit(result)
