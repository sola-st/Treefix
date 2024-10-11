# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Wrapper for tm.assert_*_equal to dispatch to the appropriate test function.

    Parameters
    ----------
    left, right : Index, Series, DataFrame, ExtensionArray, or np.ndarray
        The two items to be compared.
    **kwargs
        All keyword arguments are passed through to the underlying assert method.
    """
__tracebackhide__ = True

if isinstance(left, Index):
    assert_index_equal(left, right, **kwargs)
    if isinstance(left, (DatetimeIndex, TimedeltaIndex)):
        assert left.freq == right.freq, (left.freq, right.freq)
elif isinstance(left, Series):
    assert_series_equal(left, right, **kwargs)
elif isinstance(left, DataFrame):
    assert_frame_equal(left, right, **kwargs)
elif isinstance(left, IntervalArray):
    assert_interval_array_equal(left, right, **kwargs)
elif isinstance(left, PeriodArray):
    assert_period_array_equal(left, right, **kwargs)
elif isinstance(left, DatetimeArray):
    assert_datetime_array_equal(left, right, **kwargs)
elif isinstance(left, TimedeltaArray):
    assert_timedelta_array_equal(left, right, **kwargs)
elif isinstance(left, ExtensionArray):
    assert_extension_array_equal(left, right, **kwargs)
elif isinstance(left, np.ndarray):
    assert_numpy_array_equal(left, right, **kwargs)
elif isinstance(left, str):
    assert kwargs == {}
    assert left == right
else:
    assert kwargs == {}
    assert_almost_equal(left, right)
