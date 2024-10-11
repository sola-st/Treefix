# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
"""
    Compute a simple cross tabulation of two (or more) factors.

    By default, computes a frequency table of the factors unless an
    array of values and an aggregation function are passed.

    Parameters
    ----------
    index : array-like, Series, or list of arrays/Series
        Values to group by in the rows.
    columns : array-like, Series, or list of arrays/Series
        Values to group by in the columns.
    values : array-like, optional
        Array of values to aggregate according to the factors.
        Requires `aggfunc` be specified.
    rownames : sequence, default None
        If passed, must match number of row arrays passed.
    colnames : sequence, default None
        If passed, must match number of column arrays passed.
    aggfunc : function, optional
        If specified, requires `values` be specified as well.
    margins : bool, default False
        Add row/column margins (subtotals).
    margins_name : str, default 'All'
        Name of the row/column that will contain the totals
        when margins is True.
    dropna : bool, default True
        Do not include columns whose entries are all NaN.
    normalize : bool, {'all', 'index', 'columns'}, or {0,1}, default False
        Normalize by dividing all values by the sum of values.

        - If passed 'all' or `True`, will normalize over all values.
        - If passed 'index' will normalize over each row.
        - If passed 'columns' will normalize over each column.
        - If margins is `True`, will also normalize margin values.

    Returns
    -------
    DataFrame
        Cross tabulation of the data.

    See Also
    --------
    DataFrame.pivot : Reshape data based on column values.
    pivot_table : Create a pivot table as a DataFrame.

    Notes
    -----
    Any Series passed will have their name attributes used unless row or column
    names for the cross-tabulation are specified.

    Any input passed containing Categorical data will have **all** of its
    categories included in the cross-tabulation, even if the actual data does
    not contain any instances of a particular category.

    In the event that there aren't overlapping indexes an empty DataFrame will
    be returned.

    Reference :ref:`the user guide <reshaping.crosstabulations>` for more examples.

    Examples
    --------
    >>> a = np.array(["foo", "foo", "foo", "foo", "bar", "bar",
    ...               "bar", "bar", "foo", "foo", "foo"], dtype=object)
    >>> b = np.array(["one", "one", "one", "two", "one", "one",
    ...               "one", "two", "two", "two", "one"], dtype=object)
    >>> c = np.array(["dull", "dull", "shiny", "dull", "dull", "shiny",
    ...               "shiny", "dull", "shiny", "shiny", "shiny"],
    ...              dtype=object)
    >>> pd.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])
    b   one        two
    c   dull shiny dull shiny
    a
    bar    1     2    1     0
    foo    2     2    1     2

    Here 'c' and 'f' are not represented in the data and will not be
    shown in the output because dropna is True by default. Set
    dropna=False to preserve categories with no data.

    >>> foo = pd.Categorical(['a', 'b'], categories=['a', 'b', 'c'])
    >>> bar = pd.Categorical(['d', 'e'], categories=['d', 'e', 'f'])
    >>> pd.crosstab(foo, bar)
    col_0  d  e
    row_0
    a      1  0
    b      0  1
    >>> pd.crosstab(foo, bar, dropna=False)
    col_0  d  e  f
    row_0
    a      1  0  0
    b      0  1  0
    c      0  0  0
    """
if values is None and aggfunc is not None:
    raise ValueError("aggfunc cannot be used without values.")

if values is not None and aggfunc is None:
    raise ValueError("values cannot be used without an aggfunc.")

if not is_nested_list_like(index):
    index = [index]
if not is_nested_list_like(columns):
    columns = [columns]

common_idx = None
pass_objs = [x for x in index + columns if isinstance(x, (ABCSeries, ABCDataFrame))]
if pass_objs:
    common_idx = get_objs_combined_axis(pass_objs, intersect=True, sort=False)

rownames = _get_names(index, rownames, prefix="row")
colnames = _get_names(columns, colnames, prefix="col")

# duplicate names mapped to unique names for pivot op
(
    rownames_mapper,
    unique_rownames,
    colnames_mapper,
    unique_colnames,
) = _build_names_mapper(rownames, colnames)

from pandas import DataFrame

data = {
    **dict(zip(unique_rownames, index)),
    **dict(zip(unique_colnames, columns)),
}
df = DataFrame(data, index=common_idx)

if values is None:
    df["__dummy__"] = 0
    kwargs = {"aggfunc": len, "fill_value": 0}
else:
    df["__dummy__"] = values
    kwargs = {"aggfunc": aggfunc}

# error: Argument 7 to "pivot_table" of "DataFrame" has incompatible type
# "**Dict[str, object]"; expected "Union[...]"
table = df.pivot_table(
    "__dummy__",
    index=unique_rownames,
    columns=unique_colnames,
    margins=margins,
    margins_name=margins_name,
    dropna=dropna,
    **kwargs,  # type: ignore[arg-type]
)

# Post-process
if normalize is not False:
    table = _normalize(
        table, normalize=normalize, margins=margins, margins_name=margins_name
    )

table = table.rename_axis(index=rownames_mapper, axis=0)
table = table.rename_axis(columns=colnames_mapper, axis=1)

exit(table)
