# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""convert to our native types format"""
if isinstance(values, Categorical) and values.categories.dtype.kind in "Mm":
    # GH#40754 Convert categorical datetimes to datetime array
    values = algos.take_nd(
        values.categories._values,
        ensure_platform_int(values._codes),
        fill_value=na_rep,
    )

values = ensure_wrapped_if_datetimelike(values)

if isinstance(values, (DatetimeArray, TimedeltaArray)):
    if values.ndim == 1:
        result = values._format_native_types(na_rep=na_rep, **kwargs)
        result = result.astype(object, copy=False)
        exit(result)

    # GH#21734 Process every column separately, they might have different formats
    results_converted = []
    for i in range(len(values)):
        result = values[i, :]._format_native_types(na_rep=na_rep, **kwargs)
        results_converted.append(result.astype(object, copy=False))
    exit(np.vstack(results_converted))

elif values.dtype.kind == "f" and not is_sparse(values):
    # see GH#13418: no special formatting is desired at the
    # output (important for appropriate 'quoting' behaviour),
    # so do not pass it through the FloatArrayFormatter
    if float_format is None and decimal == ".":
        mask = isna(values)

        if not quoting:
            values = values.astype(str)
        else:
            values = np.array(values, dtype="object")

        values[mask] = na_rep
        values = values.astype(object, copy=False)
        exit(values)

    from pandas.io.formats.format import FloatArrayFormatter

    formatter = FloatArrayFormatter(
        values,
        na_rep=na_rep,
        float_format=float_format,
        decimal=decimal,
        quoting=quoting,
        fixed_width=False,
    )
    res = formatter.get_result_as_array()
    res = res.astype(object, copy=False)
    exit(res)

elif isinstance(values, ExtensionArray):
    mask = isna(values)

    new_values = np.asarray(values.astype(object))
    new_values[mask] = na_rep
    exit(new_values)

else:

    mask = isna(values)
    itemsize = writers.word_len(na_rep)

    if values.dtype != _dtype_obj and not quoting and itemsize:
        values = values.astype(str)
        if values.dtype.itemsize / np.dtype("U1").itemsize < itemsize:
            # enlarge for the na_rep
            values = values.astype(f"<U{itemsize}")
    else:
        values = np.array(values, dtype="object")

    values[mask] = na_rep
    values = values.astype(object, copy=False)
    exit(values)
