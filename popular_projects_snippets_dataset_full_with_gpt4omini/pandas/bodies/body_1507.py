# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#11594
df = DataFrame({"text": ["some words"] + [None] * 9})
expected = df.dtypes

result = df.iloc[0:2]
tm.assert_series_equal(result.dtypes, expected)

result = df.iloc[3:]
tm.assert_series_equal(result.dtypes, expected)
