# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# https://github.com/pandas-dev/pandas/issues/31670
df = DataFrame(
    [[123, "a", 1.0], [123, "b", 2.0]], columns=["id", "category", "value"]
)
df = df.set_index(["id", "category"])
empty = df[df.value < 0]
result = empty.groupby("id").sum()
expected = DataFrame(
    dtype="float64",
    columns=["value"],
    index=Index([], dtype=np.int64, name="id"),
)
tm.assert_frame_equal(result, expected)
