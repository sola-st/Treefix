# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#13672
td = Timedelta(f"1{freq}")
ts = Timestamp("1970-01-01")

idx = date_range(
    start=ts + td,
    end=ts + 4 * td,
    freq=freq,
)
exp = DatetimeIndex(
    [ts + n * td for n in range(1, 5)],
    freq=freq,
)
tm.assert_index_equal(idx, exp)

# start after end
idx = date_range(
    start=ts + 4 * td,
    end=ts + td,
    freq=freq,
)
exp = DatetimeIndex([], freq=freq)
tm.assert_index_equal(idx, exp)

# start matches end
idx = date_range(
    start=ts + td,
    end=ts + td,
    freq=freq,
)
exp = DatetimeIndex([ts + td], freq=freq)
tm.assert_index_equal(idx, exp)
