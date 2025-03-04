# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
idx = DatetimeIndex(
    [
        "2014-07-04 09:00",
        "2014-07-04 10:00",
        "2014-07-04 11:00",
        "2014-07-04 12:00",
        "2014-07-04 13:00",
        "2014-07-04 14:00",
        "2014-07-04 15:00",
        "2014-07-04 16:00",
    ],
    freq="BH",
)
rng = date_range("2014-07-04 09:00", "2014-07-04 16:00", freq="BH")
tm.assert_index_equal(idx, rng)

idx = DatetimeIndex(["2014-07-04 16:00", "2014-07-07 09:00"], freq="BH")
rng = date_range("2014-07-04 16:00", "2014-07-07 09:00", freq="BH")
tm.assert_index_equal(idx, rng)

idx = DatetimeIndex(
    [
        "2014-07-04 09:00",
        "2014-07-04 10:00",
        "2014-07-04 11:00",
        "2014-07-04 12:00",
        "2014-07-04 13:00",
        "2014-07-04 14:00",
        "2014-07-04 15:00",
        "2014-07-04 16:00",
        "2014-07-07 09:00",
        "2014-07-07 10:00",
        "2014-07-07 11:00",
        "2014-07-07 12:00",
        "2014-07-07 13:00",
        "2014-07-07 14:00",
        "2014-07-07 15:00",
        "2014-07-07 16:00",
        "2014-07-08 09:00",
        "2014-07-08 10:00",
        "2014-07-08 11:00",
        "2014-07-08 12:00",
        "2014-07-08 13:00",
        "2014-07-08 14:00",
        "2014-07-08 15:00",
        "2014-07-08 16:00",
    ],
    freq="BH",
)
rng = date_range("2014-07-04 09:00", "2014-07-08 16:00", freq="BH")
tm.assert_index_equal(idx, rng)
