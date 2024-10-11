# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
columns = list(columns)

# Convert `dtype` to a defaultdict of some kind.
# This will enable us to write `dtype[col_name]`
# without worrying about KeyError issues later on.
dtype_dict: defaultdict[Hashable, Any]
if not is_dict_like(dtype):
    # if dtype == None, default will be object.
    default_dtype = dtype or object
    dtype_dict = defaultdict(lambda: default_dtype)
else:
    dtype = cast(dict, dtype)
    dtype_dict = defaultdict(
        lambda: object,
        {columns[k] if is_integer(k) else k: v for k, v in dtype.items()},
    )

# Even though we have no data, the "index" of the empty DataFrame
# could for example still be an empty MultiIndex. Thus, we need to
# check whether we have any index columns specified, via either:
#
# 1) index_col (column indices)
# 2) index_names (column names)
#
# Both must be non-null to ensure a successful construction. Otherwise,
# we have to create a generic empty Index.
index: Index
if (index_col is None or index_col is False) or index_names is None:
    index = default_index(0)
else:
    data = [Series([], dtype=dtype_dict[name]) for name in index_names]
    index = ensure_index_from_sequences(data, names=index_names)
    index_col.sort()

    for i, n in enumerate(index_col):
        columns.pop(n - i)

col_dict = {
    col_name: Series([], dtype=dtype_dict[col_name]) for col_name in columns
}

exit((index, columns, col_dict))
