# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    Detect missing values for an array-like object.

    This function takes a scalar or array-like object and indicates
    whether values are missing (``NaN`` in numeric arrays, ``None`` or ``NaN``
    in object arrays, ``NaT`` in datetimelike).

    Parameters
    ----------
    obj : scalar or array-like
        Object to check for null or missing values.

    Returns
    -------
    bool or array-like of bool
        For scalar input, returns a scalar boolean.
        For array input, returns an array of boolean indicating whether each
        corresponding element is missing.

    See Also
    --------
    notna : Boolean inverse of pandas.isna.
    Series.isna : Detect missing values in a Series.
    DataFrame.isna : Detect missing values in a DataFrame.
    Index.isna : Detect missing values in an Index.

    Examples
    --------
    Scalar arguments (including strings) result in a scalar boolean.

    >>> pd.isna('dog')
    False

    >>> pd.isna(pd.NA)
    True

    >>> pd.isna(np.nan)
    True

    ndarrays result in an ndarray of booleans.

    >>> array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
    >>> array
    array([[ 1., nan,  3.],
           [ 4.,  5., nan]])
    >>> pd.isna(array)
    array([[False,  True, False],
           [False, False,  True]])

    For indexes, an ndarray of booleans is returned.

    >>> index = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None,
    ...                           "2017-07-08"])
    >>> index
    DatetimeIndex(['2017-07-05', '2017-07-06', 'NaT', '2017-07-08'],
                  dtype='datetime64[ns]', freq=None)
    >>> pd.isna(index)
    array([False, False,  True, False])

    For Series and DataFrame, the same type is returned, containing booleans.

    >>> df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
    >>> df
         0     1    2
    0  ant   bee  cat
    1  dog  None  fly
    >>> pd.isna(df)
           0      1      2
    0  False  False  False
    1  False   True  False

    >>> pd.isna(df[1])
    0    False
    1     True
    Name: 1, dtype: bool
    """
exit(_isna(obj))
