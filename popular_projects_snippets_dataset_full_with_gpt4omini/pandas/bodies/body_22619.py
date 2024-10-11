# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Whether each element in the DataFrame is contained in values.

        Parameters
        ----------
        values : iterable, Series, DataFrame or dict
            The result will only be true at a location if all the
            labels match. If `values` is a Series, that's the index. If
            `values` is a dict, the keys must be the column names,
            which must match. If `values` is a DataFrame,
            then both the index and column labels must match.

        Returns
        -------
        DataFrame
            DataFrame of booleans showing whether each element in the DataFrame
            is contained in values.

        See Also
        --------
        DataFrame.eq: Equality test for DataFrame.
        Series.isin: Equivalent method on Series.
        Series.str.contains: Test if pattern or regex is contained within a
            string of a Series or Index.

        Examples
        --------
        >>> df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
        ...                   index=['falcon', 'dog'])
        >>> df
                num_legs  num_wings
        falcon         2          2
        dog            4          0

        When ``values`` is a list check whether every value in the DataFrame
        is present in the list (which animals have 0 or 2 legs or wings)

        >>> df.isin([0, 2])
                num_legs  num_wings
        falcon      True       True
        dog        False       True

        To check if ``values`` is *not* in the DataFrame, use the ``~`` operator:

        >>> ~df.isin([0, 2])
                num_legs  num_wings
        falcon     False      False
        dog         True      False

        When ``values`` is a dict, we can pass values to check for each
        column separately:

        >>> df.isin({'num_wings': [0, 3]})
                num_legs  num_wings
        falcon     False      False
        dog        False       True

        When ``values`` is a Series or DataFrame the index and column must
        match. Note that 'falcon' does not match based on the number of legs
        in other.

        >>> other = pd.DataFrame({'num_legs': [8, 3], 'num_wings': [0, 2]},
        ...                      index=['spider', 'falcon'])
        >>> df.isin(other)
                num_legs  num_wings
        falcon     False       True
        dog        False      False
        """
if isinstance(values, dict):
    from pandas.core.reshape.concat import concat

    values = collections.defaultdict(list, values)
    result = concat(
        (
            self.iloc[:, [i]].isin(values[col])
            for i, col in enumerate(self.columns)
        ),
        axis=1,
    )
elif isinstance(values, Series):
    if not values.index.is_unique:
        raise ValueError("cannot compute isin with a duplicate axis.")
    result = self.eq(values.reindex_like(self), axis="index")
elif isinstance(values, DataFrame):
    if not (values.columns.is_unique and values.index.is_unique):
        raise ValueError("cannot compute isin with a duplicate axis.")
    result = self.eq(values.reindex_like(self))
else:
    if not is_list_like(values):
        raise TypeError(
            "only list-like or dict-like objects are allowed "
            "to be passed to DataFrame.isin(), "
            f"you passed a '{type(values).__name__}'"
        )
    # error: Argument 2 to "isin" has incompatible type "Union[Sequence[Any],
    # Mapping[Any, Any]]"; expected "Union[Union[ExtensionArray,
    # ndarray[Any, Any]], Index, Series]"
    result = self._constructor(
        algorithms.isin(
            self.values.ravel(), values  # type: ignore[arg-type]
        ).reshape(self.shape),
        self.index,
        self.columns,
    )
exit(result.__finalize__(self, method="isin"))
