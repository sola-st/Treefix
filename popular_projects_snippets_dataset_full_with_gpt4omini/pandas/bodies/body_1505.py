# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

# GH#12411
df = DataFrame({"date": [Timestamp("20130101").tz_localize("UTC"), pd.NaT]})
expected = df.dtypes

result = df.iloc[[0]]
tm.assert_series_equal(result.dtypes, expected)

result = df.iloc[[1]]
tm.assert_series_equal(result.dtypes, expected)
