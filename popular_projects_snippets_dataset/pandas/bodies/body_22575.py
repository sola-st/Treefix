# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Transform each element of a list-like to a row, replicating index values.

        Parameters
        ----------
        column : IndexLabel
            Column(s) to explode.
            For multiple columns, specify a non-empty list with each element
            be str or tuple, and all specified columns their list-like data
            on same row of the frame must have matching length.

            .. versionadded:: 1.3.0
                Multi-column explode

        ignore_index : bool, default False
            If True, the resulting index will be labeled 0, 1, …, n - 1.

            .. versionadded:: 1.1.0

        Returns
        -------
        DataFrame
            Exploded lists to rows of the subset columns;
            index will be duplicated for these rows.

        Raises
        ------
        ValueError :
            * If columns of the frame are not unique.
            * If specified columns to explode is empty list.
            * If specified columns to explode have not matching count of
              elements rowwise in the frame.

        See Also
        --------
        DataFrame.unstack : Pivot a level of the (necessarily hierarchical)
            index labels.
        DataFrame.melt : Unpivot a DataFrame from wide format to long format.
        Series.explode : Explode a DataFrame from list-like columns to long format.

        Notes
        -----
        This routine will explode list-likes including lists, tuples, sets,
        Series, and np.ndarray. The result dtype of the subset rows will
        be object. Scalars will be returned unchanged, and empty list-likes will
        result in a np.nan for that row. In addition, the ordering of rows in the
        output will be non-deterministic when exploding sets.

        Reference :ref:`the user guide <reshaping.explode>` for more examples.

        Examples
        --------
        >>> df = pd.DataFrame({'A': [[0, 1, 2], 'foo', [], [3, 4]],
        ...                    'B': 1,
        ...                    'C': [['a', 'b', 'c'], np.nan, [], ['d', 'e']]})
        >>> df
                   A  B          C
        0  [0, 1, 2]  1  [a, b, c]
        1        foo  1        NaN
        2         []  1         []
        3     [3, 4]  1     [d, e]

        Single-column explode.

        >>> df.explode('A')
             A  B          C
        0    0  1  [a, b, c]
        0    1  1  [a, b, c]
        0    2  1  [a, b, c]
        1  foo  1        NaN
        2  NaN  1         []
        3    3  1     [d, e]
        3    4  1     [d, e]

        Multi-column explode.

        >>> df.explode(list('AC'))
             A  B    C
        0    0  1    a
        0    1  1    b
        0    2  1    c
        1  foo  1  NaN
        2  NaN  1  NaN
        3    3  1    d
        3    4  1    e
        """
if not self.columns.is_unique:
    duplicate_cols = self.columns[self.columns.duplicated()].tolist()
    raise ValueError(
        f"DataFrame columns must be unique. Duplicate columns: {duplicate_cols}"
    )

columns: list[Hashable]
if is_scalar(column) or isinstance(column, tuple):
    columns = [column]
elif isinstance(column, list) and all(
    is_scalar(c) or isinstance(c, tuple) for c in column
):
    if not column:
        raise ValueError("column must be nonempty")
    if len(column) > len(set(column)):
        raise ValueError("column must be unique")
    columns = column
else:
    raise ValueError("column must be a scalar, tuple, or list thereof")

df = self.reset_index(drop=True)
if len(columns) == 1:
    result = df[columns[0]].explode()
else:
    mylen = lambda x: len(x) if (is_list_like(x) and len(x) > 0) else 1
    counts0 = self[columns[0]].apply(mylen)
    for c in columns[1:]:
        if not all(counts0 == self[c].apply(mylen)):
            raise ValueError("columns must have matching element counts")
    result = DataFrame({c: df[c].explode() for c in columns})
result = df.drop(columns, axis=1).join(result)
if ignore_index:
    result.index = default_index(len(result))
else:
    result.index = self.index.take(result.index)
result = result.reindex(columns=self.columns, copy=False)

exit(result.__finalize__(self, method="explode"))
