# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
idx1 = date_range(start="2014-07-04 15:00", end="2014-07-08 10:00", freq="BH")
idx2 = date_range(start="2014-07-04 15:00", periods=12, freq="BH")
idx3 = date_range(end="2014-07-08 10:00", periods=12, freq="BH")
expected = DatetimeIndex(
    [
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
    ],
    freq="BH",
)
for idx in [idx1, idx2, idx3]:
    tm.assert_index_equal(idx, expected)

idx1 = date_range(start="2014-07-04 15:45", end="2014-07-08 10:45", freq="BH")
idx2 = date_range(start="2014-07-04 15:45", periods=12, freq="BH")
idx3 = date_range(end="2014-07-08 10:45", periods=12, freq="BH")

expected = idx1
for idx in [idx1, idx2, idx3]:
    tm.assert_index_equal(idx, expected)
