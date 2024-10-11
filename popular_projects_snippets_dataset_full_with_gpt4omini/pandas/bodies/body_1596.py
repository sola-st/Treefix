# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#21846
idx = date_range(
    "2017-10-29 01:30:00", tz="Europe/Berlin", periods=5, freq="30 min"
)
series2 = Series([0, 1, 2, 3, 4], index=idx)

t_1 = Timestamp("2017-10-29 02:30:00+02:00", tz="Europe/Berlin")
t_2 = Timestamp("2017-10-29 02:00:00+01:00", tz="Europe/Berlin")
result = series2.loc[t_1:t_2]
expected = Series([2, 3], index=idx[2:4])
tm.assert_series_equal(result, expected)

result = series2[t_1]
expected = 2
assert result == expected
