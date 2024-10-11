# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#13451
df = DataFrame({"year": [2015, 2016], "month": [2, 3], "day": [4, 5]})

# int16
result = to_datetime(df.astype("int16"), cache=cache)
expected = Series(
    [Timestamp("20150204 00:00:00"), Timestamp("20160305 00:00:00")]
)
tm.assert_series_equal(result, expected)
