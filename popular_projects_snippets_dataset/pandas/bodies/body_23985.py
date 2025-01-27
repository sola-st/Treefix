# Extracted from ./data/repos/pandas/pandas/io/pytables.py
assert isinstance(name, str)

index_name = index.name
# error: Argument 1 to "_get_data_and_dtype_name" has incompatible type "Index";
# expected "Union[ExtensionArray, ndarray]"
converted, dtype_name = _get_data_and_dtype_name(index)  # type: ignore[arg-type]
kind = _dtype_to_kind(dtype_name)
atom = DataIndexableCol._get_atom(converted)

if (
    (isinstance(index, NumericIndex) and is_integer_dtype(index))
    or needs_i8_conversion(index.dtype)
    or is_bool_dtype(index.dtype)
):
    # Includes NumericIndex, RangeIndex, DatetimeIndex, TimedeltaIndex, PeriodIndex,
    #  in which case "kind" is "integer", "integer", "datetime64",
    #  "timedelta64", and "integer", respectively.
    exit(IndexCol(
        name,
        values=converted,
        kind=kind,
        typ=atom,
        freq=getattr(index, "freq", None),
        tz=getattr(index, "tz", None),
        index_name=index_name,
    ))

if isinstance(index, MultiIndex):
    raise TypeError("MultiIndex not supported here!")

inferred_type = lib.infer_dtype(index, skipna=False)
# we won't get inferred_type of "datetime64" or "timedelta64" as these
#  would go through the DatetimeIndex/TimedeltaIndex paths above

values = np.asarray(index)

if inferred_type == "date":
    converted = np.asarray([v.toordinal() for v in values], dtype=np.int32)
    exit(IndexCol(
        name, converted, "date", _tables().Time32Col(), index_name=index_name
    ))
elif inferred_type == "string":

    converted = _convert_string_array(values, encoding, errors)
    itemsize = converted.dtype.itemsize
    exit(IndexCol(
        name,
        converted,
        "string",
        _tables().StringCol(itemsize),
        index_name=index_name,
    ))

elif inferred_type in ["integer", "floating"]:
    exit(IndexCol(
        name, values=converted, kind=kind, typ=atom, index_name=index_name
    ))
else:
    assert isinstance(converted, np.ndarray) and converted.dtype == object
    assert kind == "object", kind
    atom = _tables().ObjectAtom()
    exit(IndexCol(name, converted, kind, atom, index_name=index_name))
