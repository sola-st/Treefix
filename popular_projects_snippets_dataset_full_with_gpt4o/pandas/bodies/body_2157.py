# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

result = to_datetime(
    {"year": df["year"], "month": df["month"], "day": df["day"]}, cache=cache
)
expected = Series(
    [Timestamp("20150204 00:00:00"), Timestamp("20160305 00:0:00")]
)
tm.assert_series_equal(result, expected)

# dict-like
result = to_datetime(df[["year", "month", "day"]].to_dict(), cache=cache)
tm.assert_series_equal(result, expected)
