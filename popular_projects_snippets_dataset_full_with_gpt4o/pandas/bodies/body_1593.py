# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#16896
df = DataFrame({"x": range(3)}, index=to_timedelta(range(3), unit="days"))
expected = df.iloc[0]
sliced = df.loc["0 days"]
tm.assert_series_equal(sliced, expected)
