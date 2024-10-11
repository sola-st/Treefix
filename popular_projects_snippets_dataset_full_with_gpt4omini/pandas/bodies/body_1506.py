# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#12045
df = DataFrame({"date": [datetime(2012, 1, 1), datetime(1012, 1, 2)]})
expected = df.dtypes

result = df.iloc[[0]]
tm.assert_series_equal(result.dtypes, expected)

result = df.iloc[[1]]
tm.assert_series_equal(result.dtypes, expected)
