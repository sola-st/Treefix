# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
"""
    Check the expected freq on a PeriodIndex/DatetimeIndex/TimedeltaIndex
    when the original index is _not_ generated (or generate-able) with
    period_range/date_range//timedelta_range.
    """
if isinstance(ordered, PeriodIndex):
    assert ordered.freq == orig.freq
elif isinstance(ordered, (DatetimeIndex, TimedeltaIndex)):
    assert ordered.freq is None
