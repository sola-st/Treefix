# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
if columns is lib.NoDefault:
    raise TypeError("pivot() missing 1 required argument: 'columns'")

columns_listlike = com.convert_to_list_like(columns)

# If columns is None we will create a MultiIndex level with None as name
# which might cause duplicated names because None is the default for
# level names
data.index.names = [
    name if name is not None else lib.NoDefault for name in data.index.names
]

indexed: DataFrame | Series
if values is lib.NoDefault:
    if index is not lib.NoDefault:
        cols = com.convert_to_list_like(index)
    else:
        cols = []

    append = index is lib.NoDefault
    # error: Unsupported operand types for + ("List[Any]" and "ExtensionArray")
    # error: Unsupported left operand type for + ("ExtensionArray")
    indexed = data.set_index(
        cols + columns_listlike, append=append  # type: ignore[operator]
    )
else:
    if index is lib.NoDefault:
        if isinstance(data.index, MultiIndex):
            # GH 23955
            index_list = [
                data.index.get_level_values(i) for i in range(data.index.nlevels)
            ]
        else:
            index_list = [Series(data.index, name=data.index.name)]
    else:
        index_list = [data[idx] for idx in com.convert_to_list_like(index)]

    data_columns = [data[col] for col in columns_listlike]
    index_list.extend(data_columns)
    multiindex = MultiIndex.from_arrays(index_list)

    if is_list_like(values) and not isinstance(values, tuple):
        # Exclude tuple because it is seen as a single column name
        values = cast(Sequence[Hashable], values)
        indexed = data._constructor(
            data[values]._values, index=multiindex, columns=values
        )
    else:
        indexed = data._constructor_sliced(data[values]._values, index=multiindex)
    # error: Argument 1 to "unstack" of "DataFrame" has incompatible type "Union
    # [List[Any], ExtensionArray, ndarray[Any, Any], Index, Series]"; expected
    # "Hashable"
result = indexed.unstack(columns_listlike)  # type: ignore[arg-type]
result.index.names = [
    name if name is not lib.NoDefault else None for name in result.index.names
]

exit(result)
