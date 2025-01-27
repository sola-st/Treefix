# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Detect missing values.

        Return a boolean same-sized object indicating if the values are NA.
        NA values, such as None or :attr:`numpy.NaN`, gets mapped to True
        values.
        Everything else gets mapped to False values. Characters such as empty
        strings ``''`` or :attr:`numpy.inf` are not considered NA values
        (unless you set ``pandas.options.mode.use_inf_as_na = True``).

        Returns
        -------
        {klass}
            Mask of bool values for each element in {klass} that
            indicates whether an element is an NA value.

        See Also
        --------
        {klass}.isnull : Alias of isna.
        {klass}.notna : Boolean inverse of isna.
        {klass}.dropna : Omit axes labels with missing values.
        isna : Top-level isna.

        Examples
        --------
        Show which entries in a DataFrame are NA.

        >>> df = pd.DataFrame(dict(age=[5, 6, np.NaN],
        ...                        born=[pd.NaT, pd.Timestamp('1939-05-27'),
        ...                              pd.Timestamp('1940-04-25')],
        ...                        name=['Alfred', 'Batman', ''],
        ...                        toy=[None, 'Batmobile', 'Joker']))
        >>> df
           age       born    name        toy
        0  5.0        NaT  Alfred       None
        1  6.0 1939-05-27  Batman  Batmobile
        2  NaN 1940-04-25              Joker

        >>> df.isna()
             age   born   name    toy
        0  False   True  False   True
        1  False  False  False  False
        2   True  False  False  False

        Show which entries in a Series are NA.

        >>> ser = pd.Series([5, 6, np.NaN])
        >>> ser
        0    5.0
        1    6.0
        2    NaN
        dtype: float64

        >>> ser.isna()
        0    False
        1    False
        2     True
        dtype: bool
        """
exit(isna(self).__finalize__(self, method="isna"))
