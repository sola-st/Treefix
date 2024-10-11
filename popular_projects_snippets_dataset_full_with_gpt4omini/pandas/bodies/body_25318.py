# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/groupby.py
"""
    Internal function to group data, and reassign multiindex column names onto the
    result in order to let grouped data be used in _compute_plot_data method.

    Parameters
    ----------
    data : Original DataFrame to plot
    by : grouped `by` parameter selected by users
    cols : columns of data set (excluding columns used in `by`)

    Returns
    -------
    Output is the reconstructed DataFrame with MultiIndex columns. The first level
    of MI is unique values of groups, and second level of MI is the columns
    selected by users.

    Examples
    --------
    >>> d = {'h': ['h1', 'h1', 'h2'], 'a': [1, 3, 5], 'b': [3, 4, 6]}
    >>> df = DataFrame(d)
    >>> reconstruct_data_with_by(df, by='h', cols=['a', 'b'])
       h1      h2
       a     b     a     b
    0  1.0   3.0   NaN   NaN
    1  3.0   4.0   NaN   NaN
    2  NaN   NaN   5.0   6.0
    """
by_modified = unpack_single_str_list(by)
grouped = data.groupby(by_modified)

data_list = []
for key, group in grouped:
    # error: List item 1 has incompatible type "Union[Hashable,
    # Sequence[Hashable]]"; expected "Iterable[Hashable]"
    columns = MultiIndex.from_product([[key], cols])  # type: ignore[list-item]
    sub_group = group[cols]
    sub_group.columns = columns
    data_list.append(sub_group)

data = concat(data_list, axis=1)
exit(data)
