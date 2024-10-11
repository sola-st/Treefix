# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
# used in DataFrame.__init__
# input must be a ndarray, list, Series, Index, ExtensionArray

if isinstance(values, ABCSeries):
    if columns is None:
        if values.name is not None:
            columns = Index([values.name])
    if index is None:
        index = values.index
    else:
        values = values.reindex(index)

    # zero len case (GH #2234)
    if not len(values) and columns is not None and len(columns):
        values = np.empty((0, 1), dtype=object)

    # if the array preparation does a copy -> avoid this for ArrayManager,
    # since the copy is done on conversion to 1D arrays
copy_on_sanitize = False if typ == "array" else copy

vdtype = getattr(values, "dtype", None)
if is_1d_only_ea_dtype(vdtype) or is_1d_only_ea_dtype(dtype):
    # GH#19157

    if isinstance(values, (np.ndarray, ExtensionArray)) and values.ndim > 1:
        # GH#12513 a EA dtype passed with a 2D array, split into
        #  multiple EAs that view the values
        # error: No overload variant of "__getitem__" of "ExtensionArray"
        # matches argument type "Tuple[slice, int]"
        values = [
            values[:, n]  # type: ignore[call-overload]
            for n in range(values.shape[1])
        ]
    else:
        values = [values]

    if columns is None:
        columns = Index(range(len(values)))
    else:
        columns = ensure_index(columns)

    exit(arrays_to_mgr(values, columns, index, dtype=dtype, typ=typ))

elif is_extension_array_dtype(vdtype):
    # i.e. Datetime64TZ, PeriodDtype; cases with is_1d_only_ea_dtype(vdtype)
    #  are already caught above
    values = extract_array(values, extract_numpy=True)
    if copy:
        values = values.copy()
    if values.ndim == 1:
        values = values.reshape(-1, 1)

elif isinstance(values, (np.ndarray, ExtensionArray, ABCSeries, Index)):
    # drop subclass info
    values = np.array(values, copy=copy_on_sanitize)
    values = _ensure_2d(values)

else:
    # by definition an array here
    # the dtypes will be coerced to a single dtype
    values = _prep_ndarraylike(values, copy=copy_on_sanitize)

if dtype is not None and not is_dtype_equal(values.dtype, dtype):
    # GH#40110 see similar check inside sanitize_array
    values = sanitize_array(
        values,
        None,
        dtype=dtype,
        copy=copy_on_sanitize,
        allow_2d=True,
    )

# _prep_ndarraylike ensures that values.ndim == 2 at this point
index, columns = _get_axes(
    values.shape[0], values.shape[1], index=index, columns=columns
)

_check_values_indices_shape_match(values, index, columns)

if typ == "array":

    if issubclass(values.dtype.type, str):
        values = np.array(values, dtype=object)

    if dtype is None and is_object_dtype(values.dtype):
        arrays = [
            ensure_wrapped_if_datetimelike(
                maybe_infer_to_datetimelike(values[:, i])
            )
            for i in range(values.shape[1])
        ]
    else:
        if is_datetime_or_timedelta_dtype(values.dtype):
            values = ensure_wrapped_if_datetimelike(values)
        arrays = [values[:, i] for i in range(values.shape[1])]

    if copy:
        arrays = [arr.copy() for arr in arrays]

    exit(ArrayManager(arrays, [index, columns], verify_integrity=False))

values = values.T

# if we don't have a dtype specified, then try to convert objects
# on the entire block; this is to convert if we have datetimelike's
# embedded in an object type
if dtype is None and is_object_dtype(values.dtype):
    obj_columns = list(values)
    maybe_datetime = [maybe_infer_to_datetimelike(x) for x in obj_columns]
    # don't convert (and copy) the objects if no type inference occurs
    if any(x is not y for x, y in zip(obj_columns, maybe_datetime)):
        dvals_list = [ensure_block_shape(dval, 2) for dval in maybe_datetime]
        block_values = [
            new_block_2d(dvals_list[n], placement=BlockPlacement(n))
            for n in range(len(dvals_list))
        ]
    else:
        bp = BlockPlacement(slice(len(columns)))
        nb = new_block_2d(values, placement=bp)
        block_values = [nb]
else:
    bp = BlockPlacement(slice(len(columns)))
    nb = new_block_2d(values, placement=bp)
    block_values = [nb]

if len(columns) == 0:
    block_values = []

exit(create_block_manager_from_blocks(
    block_values, [columns, index], verify_integrity=False
))
