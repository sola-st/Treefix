# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
if request.param is DatetimeIndex:
    exit(DatetimeIndex(["2000-01-04", "2000-01-01", "2000-01-02"]))
elif request.param is PeriodIndex:
    dti = DatetimeIndex(["2000-01-04", "2000-01-01", "2000-01-02"])
    exit(dti.to_period("D"))
else:
    exit(TimedeltaIndex(
        ["1 day 00:00:05", "1 day 00:00:01", "1 day 00:00:02"]
    ))
