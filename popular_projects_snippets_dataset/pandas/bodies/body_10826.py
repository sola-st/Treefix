# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 8870
d = {"foo": [10, 8, 4, 1], "bar": [10, 20, 30, 40], "baz": ["d", "c", "d", "c"]}
df = DataFrame(d)
cat = pd.cut(df["foo"], np.linspace(0, 20, 5))
df["range"] = cat
groups = df.groupby(["range", "baz"], as_index=True, sort=True)
result = groups["foo"].agg("mean")
expected = groups.agg("mean")["foo"]
tm.assert_series_equal(result, expected)
