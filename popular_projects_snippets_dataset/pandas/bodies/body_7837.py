# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
fields = [
    "year",
    "month",
    "day",
    "hour",
    "minute",
    "second",
    "weekofyear",
    "week",
    "dayofweek",
    "day_of_week",
    "dayofyear",
    "day_of_year",
    "quarter",
    "qyear",
    "days_in_month",
]

periods = list(periodindex)
ser = Series(periodindex)

for field in fields:
    field_idx = getattr(periodindex, field)
    assert len(periodindex) == len(field_idx)
    for x, val in zip(periods, field_idx):
        assert getattr(x, field) == val

    if len(ser) == 0:
        continue

    field_s = getattr(ser.dt, field)
    assert len(periodindex) == len(field_s)
    for x, val in zip(periods, field_s):
        assert getattr(x, field) == val
