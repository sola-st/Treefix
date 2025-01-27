# Extracted from ./data/repos/pandas/pandas/tests/extension/base/groupby.py
df = pd.DataFrame({"A": [1, 1, 2, 2, 3, 3, 1, 4], "B": data_for_grouping})
result = df.groupby("B", sort=False).A.mean()
_, index = pd.factorize(data_for_grouping, sort=False)

index = pd.Index(index, name="B")
expected = pd.Series([1.0, 3.0, 4.0], index=index, name="A")
self.assert_series_equal(result, expected)
