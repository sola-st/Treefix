# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Check that left and right DataFrame are equal.

    This function is intended to compare two DataFrames and output any
    differences. It is mostly intended for use in unit tests.
    Additional parameters allow varying the strictness of the
    equality checks performed.

    Parameters
    ----------
    left : DataFrame
        First DataFrame to compare.
    right : DataFrame
        Second DataFrame to compare.
    check_dtype : bool, default True
        Whether to check the DataFrame dtype is identical.
    check_index_type : bool or {'equiv'}, default 'equiv'
        Whether to check the Index class, dtype and inferred_type
        are identical.
    check_column_type : bool or {'equiv'}, default 'equiv'
        Whether to check the columns class, dtype and inferred_type
        are identical. Is passed as the ``exact`` argument of
        :func:`assert_index_equal`.
    check_frame_type : bool, default True
        Whether to check the DataFrame class is identical.
    check_names : bool, default True
        Whether to check that the `names` attribute for both the `index`
        and `column` attributes of the DataFrame is identical.
    by_blocks : bool, default False
        Specify how to compare internal data. If False, compare by columns.
        If True, compare by blocks.
    check_exact : bool, default False
        Whether to compare number exactly.
    check_datetimelike_compat : bool, default False
        Compare datetime-like which is comparable ignoring dtype.
    check_categorical : bool, default True
        Whether to compare internal Categorical exactly.
    check_like : bool, default False
        If True, ignore the order of index & columns.
        Note: index labels must match their respective rows
        (same as in columns) - same labels must be with the same data.
    check_freq : bool, default True
        Whether to check the `freq` attribute on a DatetimeIndex or TimedeltaIndex.

        .. versionadded:: 1.1.0
    check_flags : bool, default True
        Whether to check the `flags` attribute.
    rtol : float, default 1e-5
        Relative tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    obj : str, default 'DataFrame'
        Specify object name being compared, internally used to show appropriate
        assertion message.

    See Also
    --------
    assert_series_equal : Equivalent method for asserting Series equality.
    DataFrame.equals : Check DataFrame equality.

    Examples
    --------
    This example shows comparing two DataFrames that are equal
    but with columns of differing dtypes.

    >>> from pandas.testing import assert_frame_equal
    >>> df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    >>> df2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})

    df1 equals itself.

    >>> assert_frame_equal(df1, df1)

    df1 differs from df2 as column 'b' is of a different type.

    >>> assert_frame_equal(df1, df2)
    Traceback (most recent call last):
    ...
    AssertionError: Attributes of DataFrame.iloc[:, 1] (column name="b") are different

    Attribute "dtype" are different
    [left]:  int64
    [right]: float64

    Ignore differing dtypes in columns with check_dtype.

    >>> assert_frame_equal(df1, df2, check_dtype=False)
    """
__tracebackhide__ = True

# instance validation
_check_isinstance(left, right, DataFrame)

if check_frame_type:
    assert isinstance(left, type(right))
    # assert_class_equal(left, right, obj=obj)

# shape comparison
if left.shape != right.shape:
    raise_assert_detail(
        obj, f"{obj} shape mismatch", f"{repr(left.shape)}", f"{repr(right.shape)}"
    )

if check_flags:
    assert left.flags == right.flags, f"{repr(left.flags)} != {repr(right.flags)}"

# index comparison
assert_index_equal(
    left.index,
    right.index,
    exact=check_index_type,
    check_names=check_names,
    check_exact=check_exact,
    check_categorical=check_categorical,
    check_order=not check_like,
    rtol=rtol,
    atol=atol,
    obj=f"{obj}.index",
)

# column comparison
assert_index_equal(
    left.columns,
    right.columns,
    exact=check_column_type,
    check_names=check_names,
    check_exact=check_exact,
    check_categorical=check_categorical,
    check_order=not check_like,
    rtol=rtol,
    atol=atol,
    obj=f"{obj}.columns",
)

if check_like:
    left = left.reindex_like(right)

# compare by blocks
if by_blocks:
    rblocks = right._to_dict_of_blocks()
    lblocks = left._to_dict_of_blocks()
    for dtype in list(set(list(lblocks.keys()) + list(rblocks.keys()))):
        assert dtype in lblocks
        assert dtype in rblocks
        assert_frame_equal(
            lblocks[dtype], rblocks[dtype], check_dtype=check_dtype, obj=obj
        )

    # compare by columns
else:
    for i, col in enumerate(left.columns):
        # We have already checked that columns match, so we can do
        #  fast location-based lookups
        lcol = left._ixs(i, axis=1)
        rcol = right._ixs(i, axis=1)

        # GH #38183
        # use check_index=False, because we do not want to run
        # assert_index_equal for each column,
        # as we already checked it for the whole dataframe before.
        assert_series_equal(
            lcol,
            rcol,
            check_dtype=check_dtype,
            check_index_type=check_index_type,
            check_exact=check_exact,
            check_names=check_names,
            check_datetimelike_compat=check_datetimelike_compat,
            check_categorical=check_categorical,
            check_freq=check_freq,
            obj=f'{obj}.iloc[:, {i}] (column name="{col}")',
            rtol=rtol,
            atol=atol,
            check_index=False,
            check_flags=False,
        )
