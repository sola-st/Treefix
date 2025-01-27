# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Segregate Series based on type and coerce into matrices.
    Needs to handle a lot of exceptional cases.

    Used in DataFrame.__init__
    """
arrays: Sequence[Any] | Series

if columns is not None:
    from pandas.core.series import Series

    arrays = Series(data, index=columns, dtype=object)
    missing = arrays.isna()
    if index is None:
        # GH10856
        # raise ValueError if only scalars in dict
        index = _extract_index(arrays[~missing])
    else:
        index = ensure_index(index)

    # no obvious "empty" int column
    if missing.any() and not is_integer_dtype(dtype):
        nan_dtype: DtypeObj

        if dtype is not None:
            # calling sanitize_array ensures we don't mix-and-match
            #  NA dtypes
            midxs = missing.values.nonzero()[0]
            for i in midxs:
                arr = sanitize_array(arrays.iat[i], index, dtype=dtype)
                arrays.iat[i] = arr
        else:
            # GH#1783
            nan_dtype = np.dtype("object")
            val = construct_1d_arraylike_from_scalar(np.nan, len(index), nan_dtype)
            nmissing = missing.sum()
            if copy:
                rhs = [val] * nmissing
            else:
                # GH#45369
                rhs = [val.copy() for _ in range(nmissing)]
            arrays.loc[missing] = rhs

    arrays = list(arrays)
    columns = ensure_index(columns)

else:
    keys = list(data.keys())
    columns = Index(keys)
    arrays = [com.maybe_iterable_to_list(data[k]) for k in keys]
    arrays = [arr if not isinstance(arr, Index) else arr._data for arr in arrays]

if copy:
    if typ == "block":
        # We only need to copy arrays that will not get consolidated, i.e.
        #  only EA arrays
        arrays = [x.copy() if isinstance(x, ExtensionArray) else x for x in arrays]
    else:
        # dtype check to exclude e.g. range objects, scalars
        arrays = [x.copy() if hasattr(x, "dtype") else x for x in arrays]

exit(arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy))
