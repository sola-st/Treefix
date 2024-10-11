# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 44310
result = DataFrame(
    {
        "a": ["aa", "a2", "a3"],
        "b": [1, 2, 3],
    },
    index=Index(index_values),
)
expected = DataFrame(
    {
        "b_mean": [2.0, 3.0, 1.0],
    },
    index=Index(["a2", "a3", "aa"], name="a"),
)
result = result.groupby("a").apply(
    lambda df: Series([df["b"].mean()], index=["b_mean"])
)
tm.assert_frame_equal(result, expected)
