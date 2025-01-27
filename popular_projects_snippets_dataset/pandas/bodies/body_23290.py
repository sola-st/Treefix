# Extracted from ./data/repos/pandas/pandas/core/reshape/melt.py
"""
    Reshape wide-format data to long. Generalized inverse of DataFrame.pivot.

    Accepts a dictionary, ``groups``, in which each key is a new column name
    and each value is a list of old column names that will be "melted" under
    the new column name as part of the reshape.

    Parameters
    ----------
    data : DataFrame
        The wide-format DataFrame.
    groups : dict
        {new_name : list_of_columns}.
    dropna : bool, default True
        Do not include columns whose entries are all NaN.

    Returns
    -------
    DataFrame
        Reshaped DataFrame.

    See Also
    --------
    melt : Unpivot a DataFrame from wide to long format, optionally leaving
        identifiers set.
    pivot : Create a spreadsheet-style pivot table as a DataFrame.
    DataFrame.pivot : Pivot without aggregation that can handle
        non-numeric data.
    DataFrame.pivot_table : Generalization of pivot that can handle
        duplicate values for one index/column pair.
    DataFrame.unstack : Pivot based on the index values instead of a
        column.
    wide_to_long : Wide panel to long format. Less flexible but more
        user-friendly than melt.

    Examples
    --------
    >>> data = pd.DataFrame({'hr1': [514, 573], 'hr2': [545, 526],
    ...                      'team': ['Red Sox', 'Yankees'],
    ...                      'year1': [2007, 2007], 'year2': [2008, 2008]})
    >>> data
       hr1  hr2     team  year1  year2
    0  514  545  Red Sox   2007   2008
    1  573  526  Yankees   2007   2008

    >>> pd.lreshape(data, {'year': ['year1', 'year2'], 'hr': ['hr1', 'hr2']})
          team  year   hr
    0  Red Sox  2007  514
    1  Yankees  2007  573
    2  Red Sox  2008  545
    3  Yankees  2008  526
    """
if isinstance(groups, dict):
    keys = list(groups.keys())
    values = list(groups.values())
else:
    keys, values = zip(*groups)

all_cols = list(set.union(*(set(x) for x in values)))
id_cols = list(data.columns.difference(all_cols))

K = len(values[0])

for seq in values:
    if len(seq) != K:
        raise ValueError("All column lists must be same length")

mdata = {}
pivot_cols = []

for target, names in zip(keys, values):
    to_concat = [data[col]._values for col in names]

    mdata[target] = concat_compat(to_concat)
    pivot_cols.append(target)

for col in id_cols:
    mdata[col] = np.tile(data[col]._values, K)

if dropna:
    mask = np.ones(len(mdata[pivot_cols[0]]), dtype=bool)
    for c in pivot_cols:
        mask &= notna(mdata[c])
    if not mask.all():
        mdata = {k: v[mask] for k, v in mdata.items()}

exit(data._constructor(mdata, columns=id_cols + pivot_cols))
