# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH47812
ix = ["a", "b"]
id1 = pd.CategoricalIndex(ix, categories=ix)
id2 = pd.CategoricalIndex(reversed(ix), categories=reversed(ix))

df1 = DataFrame({"c1": ix}, index=id1)
df2 = DataFrame({"c2": reversed(ix)}, index=id2)
result = df1.join(df2)
expected = DataFrame(
    {"c1": ["a", "b"], "c2": ["a", "b"]},
    index=pd.CategoricalIndex(["a", "b"], categories=["a", "b"]),
)
tm.assert_frame_equal(result, expected)
