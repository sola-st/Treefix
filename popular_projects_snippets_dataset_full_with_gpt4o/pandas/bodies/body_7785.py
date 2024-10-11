# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
"""
    Check the expected freq on a PeriodIndex/DatetimeIndex/TimedeltaIndex
    when the original index is generated (or generate-able) with
    period_range/date_range/timedelta_range.
    """
if isinstance(ordered, PeriodIndex):
    assert ordered.freq == orig.freq
elif isinstance(ordered, (DatetimeIndex, TimedeltaIndex)):
    if ascending:
        assert ordered.freq.n == orig.freq.n
    else:
        assert ordered.freq.n == -1 * orig.freq.n
