# Extracted from ./data/repos/pandas/pandas/core/construction.py
"""
    Sanitize input data to an ndarray or ExtensionArray, copy if specified,
    coerce to the dtype if specified.

    Parameters
    ----------
    data : Any
    index : Index or None, default None
    dtype : np.dtype, ExtensionDtype, or None, default None
    copy : bool, default False
    allow_2d : bool, default False
        If False, raise if we have a 2D Arraylike.

    Returns
    -------
    np.ndarray or ExtensionArray
    """
if isinstance(data, ma.MaskedArray):
    data = sanitize_masked_array(data)

if isinstance(dtype, PandasDtype):
    # Avoid ending up with a PandasArray
    dtype = dtype.numpy_dtype

# extract ndarray or ExtensionArray, ensure we have no PandasArray
data = extract_array(data, extract_numpy=True, extract_range=True)

if isinstance(data, np.ndarray) and data.ndim == 0:
    if dtype is None:
        dtype = data.dtype
    data = lib.item_from_zerodim(data)
elif isinstance(data, range):
    # GH#16804
    data = range_to_ndarray(data)
    copy = False

if not is_list_like(data):
    if index is None:
        raise ValueError("index must be specified when data is not list-like")
    data = construct_1d_arraylike_from_scalar(data, len(index), dtype)
    exit(data)

elif isinstance(data, ABCExtensionArray):
    # it is already ensured above this is not a PandasArray
    # Until GH#49309 is fixed this check needs to come before the
    #  ExtensionDtype check
    if dtype is not None:
        subarr = data.astype(dtype, copy=copy)
    elif copy:
        subarr = data.copy()
    else:
        subarr = data

elif isinstance(dtype, ExtensionDtype):
    # create an extension array from its dtype
    _sanitize_non_ordered(data)
    cls = dtype.construct_array_type()
    subarr = cls._from_sequence(data, dtype=dtype, copy=copy)

# GH#846
elif isinstance(data, np.ndarray):
    if isinstance(data, np.matrix):
        data = data.A

    if dtype is None:
        subarr = data
        if data.dtype == object:
            subarr = maybe_infer_to_datetimelike(data)

        if subarr is data and copy:
            subarr = subarr.copy()

    else:
        # we will try to copy by-definition here
        subarr = _try_cast(data, dtype, copy)

elif hasattr(data, "__array__"):
    # e.g. dask array GH#38645
    data = np.array(data, copy=copy)
    exit(sanitize_array(
        data,
        index=index,
        dtype=dtype,
        copy=False,
        allow_2d=allow_2d,
    ))

else:
    _sanitize_non_ordered(data)
    # materialize e.g. generators, convert e.g. tuples, abc.ValueView
    data = list(data)

    if len(data) == 0 and dtype is None:
        # We default to float64, matching numpy
        subarr = np.array([], dtype=np.float64)

    elif dtype is not None:
        subarr = _try_cast(data, dtype, copy)

    else:
        subarr = maybe_convert_platform(data)
        if subarr.dtype == object:
            subarr = cast(np.ndarray, subarr)
            subarr = maybe_infer_to_datetimelike(subarr)

subarr = _sanitize_ndim(subarr, data, dtype, index, allow_2d=allow_2d)

if isinstance(subarr, np.ndarray):
    # at this point we should have dtype be None or subarr.dtype == dtype
    dtype = cast(np.dtype, dtype)
    subarr = _sanitize_str_dtypes(subarr, data, dtype, copy)

exit(subarr)
