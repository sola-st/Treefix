# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 24212
left = DataFrame(
    {
        "a": [1, 2, 3],
        "key": Categorical(["a", "a", "b"], categories=list("abc")),
    }
)
right = DataFrame({"b": [1, 2, 3]}, index=CategoricalIndex(["a", "b", "c"]))
result = left.merge(right, left_on="key", right_index=True, how="right")
expected = DataFrame(
    {
        "a": [1, 2, 3, None],
        "key": Categorical(["a", "a", "b", "c"]),
        "b": [1, 1, 2, 3],
    },
    index=[0, 1, 2, np.nan],
)
expected = expected.reindex(columns=["a", "key", "b"])
tm.assert_frame_equal(result, expected)
