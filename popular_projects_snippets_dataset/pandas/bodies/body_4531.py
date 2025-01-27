# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# after GH#7822
# these retain the timezones on dict construction
dr = date_range("2011/1/1", "2012/1/1", freq="W-FRI")
dr_tz = dr.tz_localize(tz)
df = DataFrame({"A": "foo", "B": dr_tz}, index=dr)
tz_expected = DatetimeTZDtype("ns", dr_tz.tzinfo)
assert df["B"].dtype == tz_expected

# GH#2810 (with timezones)
datetimes_naive = [ts.to_pydatetime() for ts in dr]
datetimes_with_tz = [ts.to_pydatetime() for ts in dr_tz]
df = DataFrame({"dr": dr})
df["dr_tz"] = dr_tz
df["datetimes_naive"] = datetimes_naive
df["datetimes_with_tz"] = datetimes_with_tz
result = df.dtypes
expected = Series(
    [
        np.dtype("datetime64[ns]"),
        DatetimeTZDtype(tz=tz),
        np.dtype("datetime64[ns]"),
        DatetimeTZDtype(tz=tz),
    ],
    index=["dr", "dr_tz", "datetimes_naive", "datetimes_with_tz"],
)
tm.assert_series_equal(result, expected)
