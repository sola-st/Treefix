# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_quarter.py
dates = [
    datetime(2016, m, d)
    for m in [10, 11, 12]
    for d in [1, 2, 3, 28, 29, 30, 31]
    if not (m == 11 and d == 31)
]
for date in dates:
    res = offset.is_on_offset(date)
    slow_version = date == (date + offset) - offset
    assert res == slow_version
