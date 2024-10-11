# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Indicate duplicate Series values.

        Duplicated values are indicated as ``True`` values in the resulting
        Series. Either all duplicates, all except the first or all except the
        last occurrence of duplicates can be indicated.

        Parameters
        ----------
        keep : {'first', 'last', False}, default 'first'
            Method to handle dropping duplicates:

            - 'first' : Mark duplicates as ``True`` except for the first
              occurrence.
            - 'last' : Mark duplicates as ``True`` except for the last
              occurrence.
            - ``False`` : Mark all duplicates as ``True``.

        Returns
        -------
        Series[bool]
            Series indicating whether each value has occurred in the
            preceding values.

        See Also
        --------
        Index.duplicated : Equivalent method on pandas.Index.
        DataFrame.duplicated : Equivalent method on pandas.DataFrame.
        Series.drop_duplicates : Remove duplicate values from Series.

        Examples
        --------
        By default, for each set of duplicated values, the first occurrence is
        set on False and all others on True:

        >>> animals = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama'])
        >>> animals.duplicated()
        0    False
        1    False
        2     True
        3    False
        4     True
        dtype: bool

        which is equivalent to

        >>> animals.duplicated(keep='first')
        0    False
        1    False
        2     True
        3    False
        4     True
        dtype: bool

        By using 'last', the last occurrence of each set of duplicated values
        is set on False and all others on True:

        >>> animals.duplicated(keep='last')
        0     True
        1    False
        2     True
        3    False
        4    False
        dtype: bool

        By setting keep on ``False``, all duplicates are True:

        >>> animals.duplicated(keep=False)
        0     True
        1    False
        2     True
        3    False
        4     True
        dtype: bool
        """
res = self._duplicated(keep=keep)
result = self._constructor(res, index=self.index)
exit(result.__finalize__(self, method="duplicated"))
