# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
"""
    Encode left and right keys as enumerated types.

    This is used to get the join indexers to be used when merging DataFrames.

    Parameters
    ----------
    lk : array-like
        Left key.
    rk : array-like
        Right key.
    sort : bool, defaults to True
        If True, the encoding is done such that the unique elements in the
        keys are sorted.
    how : {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’
        Type of merge.

    Returns
    -------
    np.ndarray[np.intp]
        Left (resp. right if called with `key='right'`) labels, as enumerated type.
    np.ndarray[np.intp]
        Right (resp. left if called with `key='right'`) labels, as enumerated type.
    int
        Number of unique elements in union of left and right labels.

    See Also
    --------
    merge : Merge DataFrame or named Series objects
        with a database-style join.
    algorithms.factorize : Encode the object as an enumerated type
        or categorical variable.

    Examples
    --------
    >>> lk = np.array(["a", "c", "b"])
    >>> rk = np.array(["a", "c"])

    Here, the unique values are `'a', 'b', 'c'`. With the default
    `sort=True`, the encoding will be `{0: 'a', 1: 'b', 2: 'c'}`:

    >>> pd.core.reshape.merge._factorize_keys(lk, rk)
    (array([0, 2, 1]), array([0, 2]), 3)

    With the `sort=False`, the encoding will correspond to the order
    in which the unique elements first appear: `{0: 'a', 1: 'c', 2: 'b'}`:

    >>> pd.core.reshape.merge._factorize_keys(lk, rk, sort=False)
    (array([0, 1, 2]), array([0, 1]), 3)
    """
# Some pre-processing for non-ndarray lk / rk
lk = extract_array(lk, extract_numpy=True, extract_range=True)
rk = extract_array(rk, extract_numpy=True, extract_range=True)
# TODO: if either is a RangeIndex, we can likely factorize more efficiently?

if isinstance(lk.dtype, DatetimeTZDtype) and isinstance(rk.dtype, DatetimeTZDtype):
    # Extract the ndarray (UTC-localized) values
    # Note: we dont need the dtypes to match, as these can still be compared
    # TODO(non-nano): need to make sure resolutions match
    lk = cast("DatetimeArray", lk)._ndarray
    rk = cast("DatetimeArray", rk)._ndarray

elif (
    is_categorical_dtype(lk.dtype)
    and is_categorical_dtype(rk.dtype)
    and is_dtype_equal(lk.dtype, rk.dtype)
):
    assert isinstance(lk, Categorical)
    assert isinstance(rk, Categorical)
    # Cast rk to encoding so we can compare codes with lk

    rk = lk._encode_with_my_categories(rk)

    lk = ensure_int64(lk.codes)
    rk = ensure_int64(rk.codes)

elif isinstance(lk, ExtensionArray) and is_dtype_equal(lk.dtype, rk.dtype):
    if not isinstance(lk, BaseMaskedArray):
        lk, _ = lk._values_for_factorize()

        # error: Item "ndarray" of "Union[Any, ndarray]" has no attribute
        # "_values_for_factorize"
        rk, _ = rk._values_for_factorize()  # type: ignore[union-attr]

klass, lk, rk = _convert_arrays_and_get_rizer_klass(lk, rk)

rizer = klass(max(len(lk), len(rk)))

if isinstance(lk, BaseMaskedArray):
    assert isinstance(rk, BaseMaskedArray)
    llab = rizer.factorize(lk._data, mask=lk._mask)
    rlab = rizer.factorize(rk._data, mask=rk._mask)
else:
    # Argument 1 to "factorize" of "ObjectFactorizer" has incompatible type
    # "Union[ndarray[Any, dtype[signedinteger[_64Bit]]],
    # ndarray[Any, dtype[object_]]]"; expected "ndarray[Any, dtype[object_]]"
    llab = rizer.factorize(lk)  # type: ignore[arg-type]
    rlab = rizer.factorize(rk)  # type: ignore[arg-type]
assert llab.dtype == np.dtype(np.intp), llab.dtype
assert rlab.dtype == np.dtype(np.intp), rlab.dtype

count = rizer.get_count()

if sort:
    uniques = rizer.uniques.to_array()
    llab, rlab = _sort_labels(uniques, llab, rlab)

# NA group
lmask = llab == -1
lany = lmask.any()
rmask = rlab == -1
rany = rmask.any()

if lany or rany:
    if lany:
        np.putmask(llab, lmask, count)
    if rany:
        np.putmask(rlab, rmask, count)
    count += 1

if how == "right":
    exit((rlab, llab, count))
exit((llab, rlab, count))
