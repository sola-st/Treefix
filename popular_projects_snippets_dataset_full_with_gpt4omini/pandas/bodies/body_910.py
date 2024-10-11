# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#25506
ts = Timestamp("2017-08-05 00:00:00+0100", tz=tz_naive_fixture)
result = Series(ts)
result.at[1] = ts
expected = Series([ts, ts])
tm.assert_series_equal(result, expected)
