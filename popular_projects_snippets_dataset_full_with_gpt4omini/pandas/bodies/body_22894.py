# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Squeeze 1 dimensional axis objects into scalars.

        Series or DataFrames with a single element are squeezed to a scalar.
        DataFrames with a single column or a single row are squeezed to a
        Series. Otherwise the object is unchanged.

        This method is most useful when you don't know if your
        object is a Series or DataFrame, but you do know it has just a single
        column. In that case you can safely call `squeeze` to ensure you have a
        Series.

        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns', None}, default None
            A specific axis to squeeze. By default, all length-1 axes are
            squeezed. For `Series` this parameter is unused and defaults to `None`.

        Returns
        -------
        DataFrame, Series, or scalar
            The projection after squeezing `axis` or all the axes.

        See Also
        --------
        Series.iloc : Integer-location based indexing for selecting scalars.
        DataFrame.iloc : Integer-location based indexing for selecting Series.
        Series.to_frame : Inverse of DataFrame.squeeze for a
            single-column DataFrame.

        Examples
        --------
        >>> primes = pd.Series([2, 3, 5, 7])

        Slicing might produce a Series with a single value:

        >>> even_primes = primes[primes % 2 == 0]
        >>> even_primes
        0    2
        dtype: int64

        >>> even_primes.squeeze()
        2

        Squeezing objects with more than one value in every axis does nothing:

        >>> odd_primes = primes[primes % 2 == 1]
        >>> odd_primes
        1    3
        2    5
        3    7
        dtype: int64

        >>> odd_primes.squeeze()
        1    3
        2    5
        3    7
        dtype: int64

        Squeezing is even more effective when used with DataFrames.

        >>> df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
        >>> df
           a  b
        0  1  2
        1  3  4

        Slicing a single column will produce a DataFrame with the columns
        having only one value:

        >>> df_a = df[['a']]
        >>> df_a
           a
        0  1
        1  3

        So the columns can be squeezed down, resulting in a Series:

        >>> df_a.squeeze('columns')
        0    1
        1    3
        Name: a, dtype: int64

        Slicing a single row from a single column will produce a single
        scalar DataFrame:

        >>> df_0a = df.loc[df.index < 1, ['a']]
        >>> df_0a
           a
        0  1

        Squeezing the rows produces a single scalar Series:

        >>> df_0a.squeeze('rows')
        a    1
        Name: 0, dtype: int64

        Squeezing all axes will project directly into a scalar:

        >>> df_0a.squeeze()
        1
        """
axes = range(self._AXIS_LEN) if axis is None else (self._get_axis_number(axis),)
exit(self.iloc[
    tuple(
        0 if i in axes and len(a) == 1 else slice(None)
        for i, a in enumerate(self.axes)
    )
])
