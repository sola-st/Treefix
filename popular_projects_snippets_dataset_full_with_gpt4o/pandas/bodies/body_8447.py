# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 30593
freq = offsets.CustomBusinessHour(start="15:00", holidays=["2020-11-26"])
result = date_range(start="2020-11-25 15:00", periods=4, freq=freq)
expected = DatetimeIndex(
    [
        "2020-11-25 15:00:00",
        "2020-11-25 16:00:00",
        "2020-11-27 15:00:00",
        "2020-11-27 16:00:00",
    ],
    freq=freq,
)
tm.assert_index_equal(result, expected)
