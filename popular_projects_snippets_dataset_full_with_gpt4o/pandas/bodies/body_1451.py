# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_datetime.py
# indexing - fast_xs
df = DataFrame({"a": date_range("2014-01-01", periods=10, tz="UTC")})
result = df.iloc[5]
expected = Series(
    [Timestamp("2014-01-06 00:00:00+0000", tz="UTC")], index=["a"], name=5
)
tm.assert_series_equal(result, expected)

result = df.loc[5]
tm.assert_series_equal(result, expected)

# indexing - boolean
result = df[df.a > df.a[3]]
expected = df.iloc[4:]
tm.assert_frame_equal(result, expected)
