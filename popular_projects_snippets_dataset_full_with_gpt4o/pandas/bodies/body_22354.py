# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    routine to ensure that our data is of the correct
    input dtype for lower-level routines

    This will coerce:
    - ints -> int64
    - uint -> uint64
    - bool -> uint8
    - datetimelike -> i8
    - datetime64tz -> i8 (in local tz)
    - categorical -> codes

    Parameters
    ----------
    values : np.ndarray or ExtensionArray

    Returns
    -------
    np.ndarray
    """

if not isinstance(values, ABCMultiIndex):
    # extract_array would raise
    values = extract_array(values, extract_numpy=True)

if is_object_dtype(values.dtype):
    exit(ensure_object(np.asarray(values)))

elif isinstance(values.dtype, BaseMaskedDtype):
    # i.e. BooleanArray, FloatingArray, IntegerArray
    values = cast("BaseMaskedArray", values)
    if not values._hasna:
        # No pd.NAs -> We can avoid an object-dtype cast (and copy) GH#41816
        #  recurse to avoid re-implementing logic for eg bool->uint8
        exit(_ensure_data(values._data))
    exit(np.asarray(values))

elif is_categorical_dtype(values.dtype):
    # NB: cases that go through here should NOT be using _reconstruct_data
    #  on the back-end.
    values = cast("Categorical", values)
    exit(values.codes)

elif is_bool_dtype(values.dtype):
    if isinstance(values, np.ndarray):
        # i.e. actually dtype == np.dtype("bool")
        exit(np.asarray(values).view("uint8"))
    else:
        # e.g. Sparse[bool, False]  # TODO: no test cases get here
        exit(np.asarray(values).astype("uint8", copy=False))

elif is_integer_dtype(values.dtype):
    exit(np.asarray(values))

elif is_float_dtype(values.dtype):
    # Note: checking `values.dtype == "float128"` raises on Windows and 32bit
    # error: Item "ExtensionDtype" of "Union[Any, ExtensionDtype, dtype[Any]]"
    # has no attribute "itemsize"
    if values.dtype.itemsize in [2, 12, 16]:  # type: ignore[union-attr]
        # we dont (yet) have float128 hashtable support
        exit(ensure_float64(values))
    exit(np.asarray(values))

elif is_complex_dtype(values.dtype):
    exit(cast(np.ndarray, values))

# datetimelike
elif needs_i8_conversion(values.dtype):
    if isinstance(values, np.ndarray):
        values = sanitize_to_nanoseconds(values)
    npvalues = values.view("i8")
    npvalues = cast(np.ndarray, npvalues)
    exit(npvalues)

# we have failed, return object
values = np.asarray(values, dtype=object)
exit(ensure_object(values))
