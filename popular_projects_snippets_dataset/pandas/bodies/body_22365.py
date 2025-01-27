# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Encode the object as an enumerated type or categorical variable.

    This method is useful for obtaining a numeric representation of an
    array when all that matters is identifying distinct values. `factorize`
    is available as both a top-level function :func:`pandas.factorize`,
    and as a method :meth:`Series.factorize` and :meth:`Index.factorize`.

    Parameters
    ----------
    {values}{sort}
    use_na_sentinel : bool, default True
        If True, the sentinel -1 will be used for NaN values. If False,
        NaN values will be encoded as non-negative integers and will not drop the
        NaN from the uniques of the values.

        .. versionadded:: 1.5.0
    {size_hint}\

    Returns
    -------
    codes : ndarray
        An integer ndarray that's an indexer into `uniques`.
        ``uniques.take(codes)`` will have the same values as `values`.
    uniques : ndarray, Index, or Categorical
        The unique valid values. When `values` is Categorical, `uniques`
        is a Categorical. When `values` is some other pandas object, an
        `Index` is returned. Otherwise, a 1-D ndarray is returned.

        .. note::

           Even if there's a missing value in `values`, `uniques` will
           *not* contain an entry for it.

    See Also
    --------
    cut : Discretize continuous-valued array.
    unique : Find the unique value in an array.

    Notes
    -----
    Reference :ref:`the user guide <reshaping.factorize>` for more examples.

    Examples
    --------
    These examples all show factorize as a top-level method like
    ``pd.factorize(values)``. The results are identical for methods like
    :meth:`Series.factorize`.

    >>> codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'b'])
    >>> codes
    array([0, 0, 1, 2, 0]...)
    >>> uniques
    array(['b', 'a', 'c'], dtype=object)

    With ``sort=True``, the `uniques` will be sorted, and `codes` will be
    shuffled so that the relationship is the maintained.

    >>> codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'b'], sort=True)
    >>> codes
    array([1, 1, 0, 2, 1]...)
    >>> uniques
    array(['a', 'b', 'c'], dtype=object)

    When ``use_na_sentinel=True`` (the default), missing values are indicated in
    the `codes` with the sentinel value ``-1`` and missing values are not
    included in `uniques`.

    >>> codes, uniques = pd.factorize(['b', None, 'a', 'c', 'b'])
    >>> codes
    array([ 0, -1,  1,  2,  0]...)
    >>> uniques
    array(['b', 'a', 'c'], dtype=object)

    Thus far, we've only factorized lists (which are internally coerced to
    NumPy arrays). When factorizing pandas objects, the type of `uniques`
    will differ. For Categoricals, a `Categorical` is returned.

    >>> cat = pd.Categorical(['a', 'a', 'c'], categories=['a', 'b', 'c'])
    >>> codes, uniques = pd.factorize(cat)
    >>> codes
    array([0, 0, 1]...)
    >>> uniques
    ['a', 'c']
    Categories (3, object): ['a', 'b', 'c']

    Notice that ``'b'`` is in ``uniques.categories``, despite not being
    present in ``cat.values``.

    For all other pandas objects, an Index of the appropriate type is
    returned.

    >>> cat = pd.Series(['a', 'a', 'c'])
    >>> codes, uniques = pd.factorize(cat)
    >>> codes
    array([0, 0, 1]...)
    >>> uniques
    Index(['a', 'c'], dtype='object')

    If NaN is in the values, and we want to include NaN in the uniques of the
    values, it can be achieved by setting ``use_na_sentinel=False``.

    >>> values = np.array([1, 2, 1, np.nan])
    >>> codes, uniques = pd.factorize(values)  # default: use_na_sentinel=True
    >>> codes
    array([ 0,  1,  0, -1])
    >>> uniques
    array([1., 2.])

    >>> codes, uniques = pd.factorize(values, use_na_sentinel=False)
    >>> codes
    array([0, 1, 0, 2])
    >>> uniques
    array([ 1.,  2., nan])
    """
# Implementation notes: This method is responsible for 3 things
# 1.) coercing data to array-like (ndarray, Index, extension array)
# 2.) factorizing codes and uniques
# 3.) Maybe boxing the uniques in an Index
#
# Step 2 is dispatched to extension types (like Categorical). They are
# responsible only for factorization. All data coercion, sorting and boxing
# should happen here.
if isinstance(values, (ABCIndex, ABCSeries)):
    exit(values.factorize(sort=sort, use_na_sentinel=use_na_sentinel))

values = _ensure_arraylike(values)
original = values

if (
    isinstance(values, (ABCDatetimeArray, ABCTimedeltaArray))
    and values.freq is not None
):
    # The presence of 'freq' means we can fast-path sorting and know there
    #  aren't NAs
    codes, uniques = values.factorize(sort=sort)
    exit((codes, uniques))

elif not isinstance(values.dtype, np.dtype):
    codes, uniques = values.factorize(use_na_sentinel=use_na_sentinel)

else:
    values = np.asarray(values)  # convert DTA/TDA/MultiIndex

    if not use_na_sentinel and is_object_dtype(values):
        # factorize can now handle differentiating various types of null values.
        # These can only occur when the array has object dtype.
        # However, for backwards compatibility we only use the null for the
        # provided dtype. This may be revisited in the future, see GH#48476.
        null_mask = isna(values)
        if null_mask.any():
            na_value = na_value_for_dtype(values.dtype, compat=False)
            # Don't modify (potentially user-provided) array
            values = np.where(null_mask, na_value, values)

    codes, uniques = factorize_array(
        values,
        use_na_sentinel=use_na_sentinel,
        size_hint=size_hint,
    )

if sort and len(uniques) > 0:
    uniques, codes = safe_sort(
        uniques,
        codes,
        use_na_sentinel=use_na_sentinel,
        assume_unique=True,
        verify=False,
    )

uniques = _reconstruct_data(uniques, original.dtype, original)

exit((codes, uniques))
