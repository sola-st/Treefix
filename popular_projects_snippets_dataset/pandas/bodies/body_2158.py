# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# dict but with constructable
df2 = df[["year", "month", "day"]].to_dict()
df2["month"] = 2
result = to_datetime(df2, cache=cache)
expected2 = Series(
    [Timestamp("20150204 00:00:00"), Timestamp("20160205 00:0:00")]
)
tm.assert_series_equal(result, expected2)
