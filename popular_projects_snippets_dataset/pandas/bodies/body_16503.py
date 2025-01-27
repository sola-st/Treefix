# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH46044
df = DataFrame({"id": ["1", "2"], "a-1": [100, 200], "a-2": [300, 400]})
df = df.astype({"id": dtype})
result = wide_to_long(
    df,
    stubnames=["a", "b"],
    i="id",
    j="num",
    sep="-",
)
index = pd.Index(
    [("1", 1), ("2", 1), ("1", 2), ("2", 2)],
    name=("id", "num"),
)
expected = DataFrame(
    {"a": [100, 200, 300, 400], "b": [np.nan] * 4},
    index=index,
)
new_level = expected.index.levels[0].astype(dtype)
expected.index = expected.index.set_levels(new_level, level=0)
tm.assert_frame_equal(result, expected)
