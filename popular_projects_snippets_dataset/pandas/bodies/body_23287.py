# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
def _convert_level_number(level_num: int, columns: Index):
    """
        Logic for converting the level number to something we can safely pass
        to swaplevel.

        If `level_num` matches a column name return the name from
        position `level_num`, otherwise return `level_num`.
        """
    if level_num in columns.names:
        exit(columns.names[level_num])

    exit(level_num)

this = frame.copy(deep=False)
mi_cols = this.columns  # cast(MultiIndex, this.columns)
assert isinstance(mi_cols, MultiIndex)  # caller is responsible

# this makes life much simpler
if level_num != mi_cols.nlevels - 1:
    # roll levels to put selected level at end
    roll_columns = mi_cols
    for i in range(level_num, mi_cols.nlevels - 1):
        # Need to check if the ints conflict with level names
        lev1 = _convert_level_number(i, roll_columns)
        lev2 = _convert_level_number(i + 1, roll_columns)
        roll_columns = roll_columns.swaplevel(lev1, lev2)
    this.columns = mi_cols = roll_columns

if not mi_cols._is_lexsorted():
    # Workaround the edge case where 0 is one of the column names,
    # which interferes with trying to sort based on the first
    # level
    level_to_sort = _convert_level_number(0, mi_cols)
    this = this.sort_index(level=level_to_sort, axis=1)
    mi_cols = this.columns

mi_cols = cast(MultiIndex, mi_cols)
new_columns = _stack_multi_column_index(mi_cols)

# time to ravel the values
new_data = {}
level_vals = mi_cols.levels[-1]
level_codes = sorted(set(mi_cols.codes[-1]))
level_vals_nan = level_vals.insert(len(level_vals), None)

level_vals_used = np.take(level_vals_nan, level_codes)
levsize = len(level_codes)
drop_cols = []
for key in new_columns:
    try:
        loc = this.columns.get_loc(key)
    except KeyError:
        drop_cols.append(key)
        continue

    # can make more efficient?
    # we almost always return a slice
    # but if unsorted can get a boolean
    # indexer
    if not isinstance(loc, slice):
        slice_len = len(loc)
    else:
        slice_len = loc.stop - loc.start

    if slice_len != levsize:
        chunk = this.loc[:, this.columns[loc]]
        chunk.columns = level_vals_nan.take(chunk.columns.codes[-1])
        value_slice = chunk.reindex(columns=level_vals_used).values
    else:
        if frame._is_homogeneous_type and is_extension_array_dtype(
            frame.dtypes.iloc[0]
        ):
            # TODO(EA2D): won't need special case, can go through .values
            #  paths below (might change to ._values)
            dtype = this[this.columns[loc]].dtypes.iloc[0]
            subset = this[this.columns[loc]]

            value_slice = dtype.construct_array_type()._concat_same_type(
                [x._values for _, x in subset.items()]
            )
            N, K = subset.shape
            idx = np.arange(N * K).reshape(K, N).T.ravel()
            value_slice = value_slice.take(idx)

        elif frame._is_mixed_type:
            value_slice = this[this.columns[loc]].values
        else:
            value_slice = this.values[:, loc]

    if value_slice.ndim > 1:
        # i.e. not extension
        value_slice = value_slice.ravel()

    new_data[key] = value_slice

if len(drop_cols) > 0:
    new_columns = new_columns.difference(drop_cols)

N = len(this)

if isinstance(this.index, MultiIndex):
    new_levels = list(this.index.levels)
    new_names = list(this.index.names)
    new_codes = [lab.repeat(levsize) for lab in this.index.codes]
else:
    old_codes, old_levels = factorize_from_iterable(this.index)
    new_levels = [old_levels]
    new_codes = [old_codes.repeat(levsize)]
    new_names = [this.index.name]  # something better?

new_levels.append(level_vals)
new_codes.append(np.tile(level_codes, N))
new_names.append(frame.columns.names[level_num])

new_index = MultiIndex(
    levels=new_levels, codes=new_codes, names=new_names, verify_integrity=False
)

result = frame._constructor(new_data, index=new_index, columns=new_columns)

# more efficient way to go about this? can do the whole masking biz but
# will only save a small amount of time...
if dropna:
    result = result.dropna(axis=0, how="all")

exit(result)
