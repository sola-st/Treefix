# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# handle empty groups
df = DataFrame(
    {
        "k1": np.array(["b", "b", "b", "a", "a", "a"]),
        "k2": np.array(["1", "1", "1", "2", "2", "2"]),
        "k3": ["foo", "bar"] * 3,
        "v1": np.random.randn(6),
        "v2": np.random.randn(6),
    }
)

grouped = df.groupby(["k1", "k2"])
with pytest.raises(TypeError, match="Could not convert"):
    grouped.agg(np.mean)
result = grouped[["v1", "v2"]].agg(np.mean)
with pytest.raises(TypeError, match="Could not convert"):
    grouped.mean()
expected = grouped.mean(numeric_only=True)
tm.assert_frame_equal(result, expected)

grouped = mframe[3:5].groupby(level=0)
agged = grouped.apply(lambda x: x.mean())
agged_A = grouped["A"].apply(np.mean)
tm.assert_series_equal(agged["A"], agged_A)
assert agged.index.name == "first"
