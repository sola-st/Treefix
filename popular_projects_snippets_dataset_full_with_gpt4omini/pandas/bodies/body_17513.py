# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_month.py
dates = (
    datetime(2007, 12, 15),
    datetime(2008, 1, 1),
    datetime(2008, 1, 15),
    datetime(2008, 2, 1),
    datetime(2008, 2, 15),
    datetime(2008, 3, 1),
    datetime(2008, 3, 15),
    datetime(2008, 4, 1),
    datetime(2008, 4, 15),
    datetime(2008, 5, 1),
    datetime(2008, 5, 15),
    datetime(2008, 6, 1),
    datetime(2008, 6, 15),
    datetime(2008, 7, 1),
    datetime(2008, 7, 15),
    datetime(2008, 8, 1),
    datetime(2008, 8, 15),
    datetime(2008, 9, 1),
    datetime(2008, 9, 15),
    datetime(2008, 10, 1),
    datetime(2008, 10, 15),
    datetime(2008, 11, 1),
    datetime(2008, 11, 15),
    datetime(2008, 12, 1),
    datetime(2008, 12, 15),
)

for base, exp_date in zip(dates[:-1], dates[1:]):
    assert_offset_equal(SemiMonthBegin(), base, exp_date)

# ensure .apply_index works as expected
shift = DatetimeIndex(dates[:-1])
with tm.assert_produces_warning(None):
    # GH#22535 check that we don't get a FutureWarning from adding
    # an integer array to PeriodIndex
    result = SemiMonthBegin() + shift

exp = DatetimeIndex(dates[1:])
tm.assert_index_equal(result, exp)

# ensure generating a range with DatetimeIndex gives same result
result = date_range(start=dates[0], end=dates[-1], freq="SMS")
exp = DatetimeIndex(dates, freq="SMS")
tm.assert_index_equal(result, exp)
