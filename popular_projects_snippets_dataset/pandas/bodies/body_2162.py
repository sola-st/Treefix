# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# passing coerce
df2 = DataFrame({"year": [2015, 2016], "month": [2, 20], "day": [4, 5]})

msg = (
    r'^cannot assemble the datetimes: time data ".+" doesn\'t '
    r'match format "%Y%m%d", at position 1$'
)
with pytest.raises(ValueError, match=msg):
    to_datetime(df2, cache=cache)

result = to_datetime(df2, errors="coerce", cache=cache)
expected = Series([Timestamp("20150204 00:00:00"), NaT])
tm.assert_series_equal(result, expected)
