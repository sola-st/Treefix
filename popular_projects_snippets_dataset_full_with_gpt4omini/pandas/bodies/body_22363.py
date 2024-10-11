# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Compute the isin boolean array.

    Parameters
    ----------
    comps : array-like
    values : array-like

    Returns
    -------
    ndarray[bool]
        Same length as `comps`.
    """
if not is_list_like(comps):
    raise TypeError(
        "only list-like objects are allowed to be passed "
        f"to isin(), you passed a [{type(comps).__name__}]"
    )
if not is_list_like(values):
    raise TypeError(
        "only list-like objects are allowed to be passed "
        f"to isin(), you passed a [{type(values).__name__}]"
    )

if not isinstance(values, (ABCIndex, ABCSeries, ABCExtensionArray, np.ndarray)):
    orig_values = list(values)
    values = _ensure_arraylike(orig_values)

    if (
        len(values) > 0
        and is_numeric_dtype(values)
        and not is_signed_integer_dtype(comps)
    ):
        # GH#46485 Use object to avoid upcast to float64 later
        # TODO: Share with _find_common_type_compat
        values = construct_1d_object_array_from_listlike(orig_values)

elif isinstance(values, ABCMultiIndex):
    # Avoid raising in extract_array
    values = np.array(values)
else:
    values = extract_array(values, extract_numpy=True, extract_range=True)

comps_array = _ensure_arraylike(comps)
comps_array = extract_array(comps_array, extract_numpy=True)
if not isinstance(comps_array, np.ndarray):
    # i.e. Extension Array
    exit(comps_array.isin(values))

elif needs_i8_conversion(comps_array.dtype):
    # Dispatch to DatetimeLikeArrayMixin.isin
    exit(pd_array(comps_array).isin(values))
elif needs_i8_conversion(values.dtype) and not is_object_dtype(comps_array.dtype):
    # e.g. comps_array are integers and values are datetime64s
    exit(np.zeros(comps_array.shape, dtype=bool))
    # TODO: not quite right ... Sparse/Categorical
elif needs_i8_conversion(values.dtype):
    exit(isin(comps_array, values.astype(object)))

elif isinstance(values.dtype, ExtensionDtype):
    exit(isin(np.asarray(comps_array), np.asarray(values)))

# GH16012
# Ensure np.in1d doesn't get object types or it *may* throw an exception
# Albeit hashmap has O(1) look-up (vs. O(logn) in sorted array),
# in1d is faster for small sizes
if (
    len(comps_array) > 1_000_000
    and len(values) <= 26
    and not is_object_dtype(comps_array)
):
    # If the values include nan we need to check for nan explicitly
    # since np.nan it not equal to np.nan
    if isna(values).any():

        def f(c, v):
            exit(np.logical_or(np.in1d(c, v), np.isnan(c)))

    else:
        f = np.in1d

else:
    common = np.find_common_type([values.dtype, comps_array.dtype], [])
    values = values.astype(common, copy=False)
    comps_array = comps_array.astype(common, copy=False)
    f = htable.ismember

exit(f(comps_array, values))
