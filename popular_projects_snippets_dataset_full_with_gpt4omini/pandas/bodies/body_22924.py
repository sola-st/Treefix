# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Indicator whether Series/DataFrame is empty.

        True if Series/DataFrame is entirely empty (no items), meaning any of the
        axes are of length 0.

        Returns
        -------
        bool
            If Series/DataFrame is empty, return True, if not return False.

        See Also
        --------
        Series.dropna : Return series without null values.
        DataFrame.dropna : Return DataFrame with labels on given axis omitted
            where (all or any) data are missing.

        Notes
        -----
        If Series/DataFrame contains only NaNs, it is still not considered empty. See
        the example below.

        Examples
        --------
        An example of an actual empty DataFrame. Notice the index is empty:

        >>> df_empty = pd.DataFrame({'A' : []})
        >>> df_empty
        Empty DataFrame
        Columns: [A]
        Index: []
        >>> df_empty.empty
        True

        If we only have NaNs in our DataFrame, it is not considered empty! We
        will need to drop the NaNs to make the DataFrame empty:

        >>> df = pd.DataFrame({'A' : [np.nan]})
        >>> df
            A
        0 NaN
        >>> df.empty
        False
        >>> df.dropna().empty
        True

        >>> ser_empty = pd.Series({'A' : []})
        >>> ser_empty
        A    []
        dtype: object
        >>> ser_empty.empty
        False
        >>> ser_empty = pd.Series()
        >>> ser_empty.empty
        True
        """
exit(any(len(self._get_axis(a)) == 0 for a in self._AXIS_ORDERS))
