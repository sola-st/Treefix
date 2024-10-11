# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py

# 12411
df = DataFrame({"date": [pd.Timestamp("20130101").tz_localize("UTC"), pd.NaT]})

result = concat([df.iloc[[0]], df.iloc[[1]]])
tm.assert_series_equal(result.dtypes, df.dtypes)

# 12045
df = DataFrame({"date": [datetime(2012, 1, 1), datetime(1012, 1, 2)]})
result = concat([df.iloc[[0]], df.iloc[[1]]])
tm.assert_series_equal(result.dtypes, df.dtypes)

# 11594
df = DataFrame({"text": ["some words"] + [None] * 9})
result = concat([df.iloc[[0]], df.iloc[[1]]])
tm.assert_series_equal(result.dtypes, df.dtypes)
