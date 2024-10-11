# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
"""
    Helper of :func:`pandas.pivot_table` for any non-list ``aggfunc``.
    """
keys = index + columns

values_passed = values is not None
if values_passed:
    if is_list_like(values):
        values_multi = True
        values = list(values)
    else:
        values_multi = False
        values = [values]

    # GH14938 Make sure value labels are in data
    for i in values:
        if i not in data:
            raise KeyError(i)

    to_filter = []
    for x in keys + values:
        if isinstance(x, Grouper):
            x = x.key
        try:
            if x in data:
                to_filter.append(x)
        except TypeError:
            pass
    if len(to_filter) < len(data.columns):
        data = data[to_filter]

else:
    values = data.columns
    for key in keys:
        try:
            values = values.drop(key)
        except (TypeError, ValueError, KeyError):
            pass
    values = list(values)

grouped = data.groupby(keys, observed=observed, sort=sort)
agged = grouped.agg(aggfunc)

if dropna and isinstance(agged, ABCDataFrame) and len(agged.columns):
    agged = agged.dropna(how="all")

    # gh-21133
    # we want to down cast if
    # the original values are ints
    # as we grouped with a NaN value
    # and then dropped, coercing to floats
    for v in values:
        if (
            v in data
            and is_integer_dtype(data[v])
            and v in agged
            and not is_integer_dtype(agged[v])
        ):
            if not isinstance(agged[v], ABCDataFrame) and isinstance(
                data[v].dtype, np.dtype
            ):
                # exclude DataFrame case bc maybe_downcast_to_dtype expects
                #  ArrayLike
                # e.g. test_pivot_table_multiindex_columns_doctest_case
                #  agged.columns is a MultiIndex and 'v' is indexing only
                #  on its first level.
                agged[v] = maybe_downcast_to_dtype(agged[v], data[v].dtype)

table = agged

# GH17038, this check should only happen if index is defined (not None)
if table.index.nlevels > 1 and index:
    # Related GH #17123
    # If index_names are integers, determine whether the integers refer
    # to the level position or name.
    index_names = agged.index.names[: len(index)]
    to_unstack = []
    for i in range(len(index), len(keys)):
        name = agged.index.names[i]
        if name is None or name in index_names:
            to_unstack.append(i)
        else:
            to_unstack.append(name)
    table = agged.unstack(to_unstack)

if not dropna:
    if isinstance(table.index, MultiIndex):
        m = MultiIndex.from_arrays(
            cartesian_product(table.index.levels), names=table.index.names
        )
        table = table.reindex(m, axis=0)

    if isinstance(table.columns, MultiIndex):
        m = MultiIndex.from_arrays(
            cartesian_product(table.columns.levels), names=table.columns.names
        )
        table = table.reindex(m, axis=1)

if sort is True and isinstance(table, ABCDataFrame):
    table = table.sort_index(axis=1)

if fill_value is not None:
    table = table.fillna(fill_value, downcast="infer")

if margins:
    if dropna:
        data = data[data.notna().all(axis=1)]
    table = _add_margins(
        table,
        data,
        values,
        rows=index,
        cols=columns,
        aggfunc=aggfunc,
        observed=dropna,
        margins_name=margins_name,
        fill_value=fill_value,
    )

# discard the top level
if values_passed and not values_multi and table.columns.nlevels > 1:
    table = table.droplevel(0, axis=1)
if len(index) == 0 and len(columns) > 0:
    table = table.T

# GH 15193 Make sure empty columns are removed if dropna=True
if isinstance(table, ABCDataFrame) and dropna:
    table = table.dropna(how="all", axis=1)

exit(table)
