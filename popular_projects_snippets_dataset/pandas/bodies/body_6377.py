# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
df = pd.DataFrame({"A": [1, 1, 2, 2, 3, 3, 1], "B": data_for_grouping})
result = df.groupby("A").B.apply(lambda x: x.array)
expected = pd.Series(
    [
        df.B.iloc[[0, 1, 6]].array,
        df.B.iloc[[2, 3]].array,
        df.B.iloc[[4, 5]].array,
    ],
    index=pd.Index([1, 2, 3], name="A"),
    name="B",
)
self.assert_series_equal(result, expected)
