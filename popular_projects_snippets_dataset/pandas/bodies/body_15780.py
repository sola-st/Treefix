# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# pre-2.0 this raised ValueError bc of tz mismatch
# xref GH#32581
ts = Timestamp("2016-01-04 05:06:07", tz="US/Pacific")
ts2 = ts.tz_convert("Asia/Tokyo")

ser = Series([ts, ts2], dtype=object)
res = ser.astype("datetime64[ns, Europe/Brussels]")
expected = Series(
    [ts.tz_convert("Europe/Brussels"), ts2.tz_convert("Europe/Brussels")],
    dtype="datetime64[ns, Europe/Brussels]",
)
tm.assert_series_equal(res, expected)
