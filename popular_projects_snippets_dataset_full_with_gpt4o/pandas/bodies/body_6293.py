# Extracted from ./data/repos/pandas/pandas/tests/extension/base/groupby.py
df = pd.DataFrame({"A": [1, 1, 2, 2, 3, 3, 1, 4], "B": data_for_grouping})
result = df.groupby("B", as_index=as_index).A.mean()
_, uniques = pd.factorize(data_for_grouping, sort=True)

if as_index:
    index = pd.Index(uniques, name="B")
    expected = pd.Series([3.0, 1.0, 4.0], index=index, name="A")
    self.assert_series_equal(result, expected)
else:
    expected = pd.DataFrame({"B": uniques, "A": [3.0, 1.0, 4.0]})
    self.assert_frame_equal(result, expected)
