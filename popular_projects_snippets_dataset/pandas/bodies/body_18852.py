# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Check that left and right ExtensionArrays are equal.

    Parameters
    ----------
    left, right : ExtensionArray
        The two arrays to compare.
    check_dtype : bool, default True
        Whether to check if the ExtensionArray dtypes are identical.
    index_values : numpy.ndarray, default None
        Optional index (shared by both left and right), used in output.
    check_exact : bool, default False
        Whether to compare number exactly.
    rtol : float, default 1e-5
        Relative tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    obj : str, default 'ExtensionArray'
        Specify object name being compared, internally used to show appropriate
        assertion message.

        .. versionadded:: 2.0.0

    Notes
    -----
    Missing values are checked separately from valid values.
    A mask of missing values is computed for each and checked to match.
    The remaining all-valid values are cast to object dtype and checked.

    Examples
    --------
    >>> from pandas import testing as tm
    >>> a = pd.Series([1, 2, 3, 4])
    >>> b, c = a.array, a.array
    >>> tm.assert_extension_array_equal(b, c)
    """
assert isinstance(left, ExtensionArray), "left is not an ExtensionArray"
assert isinstance(right, ExtensionArray), "right is not an ExtensionArray"
if check_dtype:
    assert_attr_equal("dtype", left, right, obj=f"Attributes of {obj}")

if (
    isinstance(left, DatetimeLikeArrayMixin)
    and isinstance(right, DatetimeLikeArrayMixin)
    and type(right) == type(left)
):
    # Avoid slow object-dtype comparisons
    # np.asarray for case where we have a np.MaskedArray
    assert_numpy_array_equal(
        np.asarray(left.asi8),
        np.asarray(right.asi8),
        index_values=index_values,
        obj=obj,
    )
    exit()

left_na = np.asarray(left.isna())
right_na = np.asarray(right.isna())
assert_numpy_array_equal(
    left_na, right_na, obj=f"{obj} NA mask", index_values=index_values
)

left_valid = left[~left_na].to_numpy(dtype=object)
right_valid = right[~right_na].to_numpy(dtype=object)
if check_exact:
    assert_numpy_array_equal(
        left_valid, right_valid, obj=obj, index_values=index_values
    )
else:
    _testing.assert_almost_equal(
        left_valid,
        right_valid,
        check_dtype=bool(check_dtype),
        rtol=rtol,
        atol=atol,
        obj=obj,
        index_values=index_values,
    )
