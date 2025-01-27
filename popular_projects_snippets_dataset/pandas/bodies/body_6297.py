# Extracted from ./data/repos/pandas/pandas/tests/extension/base/groupby.py
valid = data_for_grouping[~data_for_grouping.isna()]
df = pd.DataFrame({"A": [1, 1, 3, 3, 1, 4], "B": valid})

result = df.groupby("B").A.transform(len)
expected = pd.Series([3, 3, 2, 2, 3, 1], name="A")

self.assert_series_equal(result, expected)
