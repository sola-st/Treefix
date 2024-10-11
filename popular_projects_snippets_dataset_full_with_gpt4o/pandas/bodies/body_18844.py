# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Test that two IntervalArrays are equivalent.

    Parameters
    ----------
    left, right : IntervalArray
        The IntervalArrays to compare.
    exact : bool or {'equiv'}, default 'equiv'
        Whether to check the Index class, dtype and inferred_type
        are identical. If 'equiv', then RangeIndex can be substituted for
        NumericIndex with an int64 dtype as well.
    obj : str, default 'IntervalArray'
        Specify object name being compared, internally used to show appropriate
        assertion message
    """
_check_isinstance(left, right, IntervalArray)

kwargs = {}
if left._left.dtype.kind in ["m", "M"]:
    # We have a DatetimeArray or TimedeltaArray
    kwargs["check_freq"] = False

assert_equal(left._left, right._left, obj=f"{obj}.left", **kwargs)
assert_equal(left._right, right._right, obj=f"{obj}.left", **kwargs)

assert_attr_equal("closed", left, right, obj=obj)
