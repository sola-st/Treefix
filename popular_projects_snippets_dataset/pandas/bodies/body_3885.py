# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 19966
idx = MultiIndex.from_product(
    [["a", "b", "c"], [1, 2, 3]], names=[("A", "a"), ("B", "b")]
)
df = DataFrame({"d": [1] * 9, "e": [2] * 9}, index=idx)
result = df.unstack(("A", "a"))

expected = DataFrame(
    [[1, 1, 1, 2, 2, 2], [1, 1, 1, 2, 2, 2], [1, 1, 1, 2, 2, 2]],
    columns=MultiIndex.from_tuples(
        [
            ("d", "a"),
            ("d", "b"),
            ("d", "c"),
            ("e", "a"),
            ("e", "b"),
            ("e", "c"),
        ],
        names=[None, ("A", "a")],
    ),
    index=Index([1, 2, 3], name=("B", "b")),
)
tm.assert_frame_equal(result, expected)
