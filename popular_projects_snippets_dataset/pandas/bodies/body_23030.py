# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Return the last row(s) without any NaNs before `where`.

        The last row (for each element in `where`, if list) without any
        NaN is taken.
        In case of a :class:`~pandas.DataFrame`, the last row without NaN
        considering only the subset of columns (if not `None`)

        If there is no good value, NaN is returned for a Series or
        a Series of NaN values for a DataFrame

        Parameters
        ----------
        where : date or array-like of dates
            Date(s) before which the last row(s) are returned.
        subset : str or array-like of str, default `None`
            For DataFrame, if not `None`, only use these columns to
            check for NaNs.

        Returns
        -------
        scalar, Series, or DataFrame

            The return can be:

            * scalar : when `self` is a Series and `where` is a scalar
            * Series: when `self` is a Series and `where` is an array-like,
              or when `self` is a DataFrame and `where` is a scalar
            * DataFrame : when `self` is a DataFrame and `where` is an
              array-like

            Return scalar, Series, or DataFrame.

        See Also
        --------
        merge_asof : Perform an asof merge. Similar to left join.

        Notes
        -----
        Dates are assumed to be sorted. Raises if this is not the case.

        Examples
        --------
        A Series and a scalar `where`.

        >>> s = pd.Series([1, 2, np.nan, 4], index=[10, 20, 30, 40])
        >>> s
        10    1.0
        20    2.0
        30    NaN
        40    4.0
        dtype: float64

        >>> s.asof(20)
        2.0

        For a sequence `where`, a Series is returned. The first value is
        NaN, because the first element of `where` is before the first
        index value.

        >>> s.asof([5, 20])
        5     NaN
        20    2.0
        dtype: float64

        Missing values are not considered. The following is ``2.0``, not
        NaN, even though NaN is at the index location for ``30``.

        >>> s.asof(30)
        2.0

        Take all columns into consideration

        >>> df = pd.DataFrame({'a': [10, 20, 30, 40, 50],
        ...                    'b': [None, None, None, None, 500]},
        ...                   index=pd.DatetimeIndex(['2018-02-27 09:01:00',
        ...                                           '2018-02-27 09:02:00',
        ...                                           '2018-02-27 09:03:00',
        ...                                           '2018-02-27 09:04:00',
        ...                                           '2018-02-27 09:05:00']))
        >>> df.asof(pd.DatetimeIndex(['2018-02-27 09:03:30',
        ...                           '2018-02-27 09:04:30']))
                              a   b
        2018-02-27 09:03:30 NaN NaN
        2018-02-27 09:04:30 NaN NaN

        Take a single column into consideration

        >>> df.asof(pd.DatetimeIndex(['2018-02-27 09:03:30',
        ...                           '2018-02-27 09:04:30']),
        ...         subset=['a'])
                              a   b
        2018-02-27 09:03:30  30 NaN
        2018-02-27 09:04:30  40 NaN
        """
if isinstance(where, str):
    where = Timestamp(where)

if not self.index.is_monotonic_increasing:
    raise ValueError("asof requires a sorted index")

is_series = isinstance(self, ABCSeries)
if is_series:
    if subset is not None:
        raise ValueError("subset is not valid for Series")
else:
    if subset is None:
        subset = self.columns
    if not is_list_like(subset):
        subset = [subset]

is_list = is_list_like(where)
if not is_list:
    start = self.index[0]
    if isinstance(self.index, PeriodIndex):
        where = Period(where, freq=self.index.freq)

    if where < start:
        if not is_series:
            exit(self._constructor_sliced(
                index=self.columns, name=where, dtype=np.float64
            ))
        exit(np.nan)

    # It's always much faster to use a *while* loop here for
    # Series than pre-computing all the NAs. However a
    # *while* loop is extremely expensive for DataFrame
    # so we later pre-compute all the NAs and use the same
    # code path whether *where* is a scalar or list.
    # See PR: https://github.com/pandas-dev/pandas/pull/14476
    if is_series:
        loc = self.index.searchsorted(where, side="right")
        if loc > 0:
            loc -= 1

        values = self._values
        while loc > 0 and isna(values[loc]):
            loc -= 1
        exit(values[loc])

if not isinstance(where, Index):
    where = Index(where) if is_list else Index([where])

nulls = self.isna() if is_series else self[subset].isna().any(axis=1)
if nulls.all():
    if is_series:
        self = cast("Series", self)
        exit(self._constructor(np.nan, index=where, name=self.name))
    elif is_list:
        self = cast("DataFrame", self)
        exit(self._constructor(np.nan, index=where, columns=self.columns))
    else:
        self = cast("DataFrame", self)
        exit(self._constructor_sliced(
            np.nan, index=self.columns, name=where[0]
        ))

locs = self.index.asof_locs(where, ~(nulls._values))

# mask the missing
missing = locs == -1
data = self.take(locs)
data.index = where
if missing.any():
    # GH#16063 only do this setting when necessary, otherwise
    #  we'd cast e.g. bools to floats
    data.loc[missing] = np.nan
exit(data if is_list else data.iloc[-1])
