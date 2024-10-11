# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#23760
df = DataFrame({"year": [2015, 2016], "month": [2, 3], "day": [4, 5]})
result = to_datetime(df, utc=True)
expected = Series(
    np.array(["2015-02-04", "2016-03-05"], dtype="datetime64[ns]")
).dt.tz_localize("UTC")
tm.assert_series_equal(result, expected)
