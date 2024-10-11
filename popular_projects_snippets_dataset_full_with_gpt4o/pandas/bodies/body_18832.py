# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Check that the left and right objects are approximately equal.

    By approximately equal, we refer to objects that are numbers or that
    contain numbers which may be equivalent to specific levels of precision.

    Parameters
    ----------
    left : object
    right : object
    check_dtype : bool or {'equiv'}, default 'equiv'
        Check dtype if both a and b are the same type. If 'equiv' is passed in,
        then `RangeIndex` and `NumericIndex` with int64 dtype are also considered
        equivalent when doing type checking.
    rtol : float, default 1e-5
        Relative tolerance.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance.

        .. versionadded:: 1.1.0
    """
if isinstance(left, Index):
    assert_index_equal(
        left,
        right,
        check_exact=False,
        exact=check_dtype,
        rtol=rtol,
        atol=atol,
        **kwargs,
    )

elif isinstance(left, Series):
    assert_series_equal(
        left,
        right,
        check_exact=False,
        check_dtype=check_dtype,
        rtol=rtol,
        atol=atol,
        **kwargs,
    )

elif isinstance(left, DataFrame):
    assert_frame_equal(
        left,
        right,
        check_exact=False,
        check_dtype=check_dtype,
        rtol=rtol,
        atol=atol,
        **kwargs,
    )

else:
    # Other sequences.
    if check_dtype:
        if is_number(left) and is_number(right):
            # Do not compare numeric classes, like np.float64 and float.
            pass
        elif is_bool(left) and is_bool(right):
            # Do not compare bool classes, like np.bool_ and bool.
            pass
        else:
            if isinstance(left, np.ndarray) or isinstance(right, np.ndarray):
                obj = "numpy array"
            else:
                obj = "Input"
            assert_class_equal(left, right, obj=obj)

        # if we have "equiv", this becomes True
    _testing.assert_almost_equal(
        left, right, check_dtype=bool(check_dtype), rtol=rtol, atol=atol, **kwargs
    )
