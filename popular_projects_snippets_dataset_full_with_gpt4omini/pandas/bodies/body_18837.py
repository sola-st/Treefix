# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Check that left and right Index are equal.

    Parameters
    ----------
    left : Index
    right : Index
    exact : bool or {'equiv'}, default 'equiv'
        Whether to check the Index class, dtype and inferred_type
        are identical. If 'equiv', then RangeIndex can be substituted for
        NumericIndex with an int64 dtype as well.
    check_names : bool, default True
        Whether to check the names attribute.
    check_exact : bool, default True
        Whether to compare number exactly.
    check_categorical : bool, default True
        Whether to compare internal Categorical exactly.
    check_order : bool, default True
        Whether to compare the order of index entries as well as their values.
        If True, both indexes must contain the same elements, in the same order.
        If False, both indexes must contain the same elements, but in any order.

        .. versionadded:: 1.2.0
    rtol : float, default 1e-5
        Relative tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    obj : str, default 'Index'
        Specify object name being compared, internally used to show appropriate
        assertion message.

    Examples
    --------
    >>> from pandas import testing as tm
    >>> a = pd.Index([1, 2, 3])
    >>> b = pd.Index([1, 2, 3])
    >>> tm.assert_index_equal(a, b)
    """
__tracebackhide__ = True

def _check_types(left, right, obj: str = "Index") -> None:
    if not exact:
        exit()

    assert_class_equal(left, right, exact=exact, obj=obj)
    assert_attr_equal("inferred_type", left, right, obj=obj)

    # Skip exact dtype checking when `check_categorical` is False
    if is_categorical_dtype(left.dtype) and is_categorical_dtype(right.dtype):
        if check_categorical:
            assert_attr_equal("dtype", left, right, obj=obj)
            assert_index_equal(left.categories, right.categories, exact=exact)
        exit()

    assert_attr_equal("dtype", left, right, obj=obj)

def _get_ilevel_values(index, level):
    # accept level number only
    unique = index.levels[level]
    level_codes = index.codes[level]
    filled = take_nd(unique._values, level_codes, fill_value=unique._na_value)
    exit(unique._shallow_copy(filled, name=index.names[level]))

# instance validation
_check_isinstance(left, right, Index)

# class / dtype comparison
_check_types(left, right, obj=obj)

# level comparison
if left.nlevels != right.nlevels:
    msg1 = f"{obj} levels are different"
    msg2 = f"{left.nlevels}, {left}"
    msg3 = f"{right.nlevels}, {right}"
    raise_assert_detail(obj, msg1, msg2, msg3)

# length comparison
if len(left) != len(right):
    msg1 = f"{obj} length are different"
    msg2 = f"{len(left)}, {left}"
    msg3 = f"{len(right)}, {right}"
    raise_assert_detail(obj, msg1, msg2, msg3)

# If order doesn't matter then sort the index entries
if not check_order:
    left = safe_sort_index(left)
    right = safe_sort_index(right)

# MultiIndex special comparison for little-friendly error messages
if left.nlevels > 1:
    left = cast(MultiIndex, left)
    right = cast(MultiIndex, right)

    for level in range(left.nlevels):
        # cannot use get_level_values here because it can change dtype
        llevel = _get_ilevel_values(left, level)
        rlevel = _get_ilevel_values(right, level)

        lobj = f"MultiIndex level [{level}]"
        assert_index_equal(
            llevel,
            rlevel,
            exact=exact,
            check_names=check_names,
            check_exact=check_exact,
            rtol=rtol,
            atol=atol,
            obj=lobj,
        )
        # get_level_values may change dtype
        _check_types(left.levels[level], right.levels[level], obj=obj)

    # skip exact index checking when `check_categorical` is False
if check_exact and check_categorical:
    if not left.equals(right):
        mismatch = left._values != right._values

        if is_extension_array_dtype(mismatch):
            mismatch = cast("ExtensionArray", mismatch).fillna(True)

        diff = np.sum(mismatch.astype(int)) * 100.0 / len(left)
        msg = f"{obj} values are different ({np.round(diff, 5)} %)"
        raise_assert_detail(obj, msg, left, right)
else:

    # if we have "equiv", this becomes True
    exact_bool = bool(exact)
    _testing.assert_almost_equal(
        left.values,
        right.values,
        rtol=rtol,
        atol=atol,
        check_dtype=exact_bool,
        obj=obj,
        lobj=left,
        robj=right,
    )

# metadata comparison
if check_names:
    assert_attr_equal("names", left, right, obj=obj)
if isinstance(left, PeriodIndex) or isinstance(right, PeriodIndex):
    assert_attr_equal("freq", left, right, obj=obj)
if isinstance(left, IntervalIndex) or isinstance(right, IntervalIndex):
    assert_interval_array_equal(left._values, right._values)

if check_categorical:
    if is_categorical_dtype(left.dtype) or is_categorical_dtype(right.dtype):
        assert_categorical_equal(left._values, right._values, obj=f"{obj} category")
