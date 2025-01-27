# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# mixed dtypes
df = DataFrame({"year": [2015, 2016], "month": [2, 3], "day": [4, 5]})
df["month"] = df["month"].astype("int8")
df["day"] = df["day"].astype("int8")
result = to_datetime(df, cache=cache)
expected = Series(
    [Timestamp("20150204 00:00:00"), Timestamp("20160305 00:00:00")]
)
tm.assert_series_equal(result, expected)
