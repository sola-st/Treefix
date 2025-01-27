# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# PH 28306: Unstack df with multi level cols and rows
df = DataFrame(
    [[1, 2], [3, 4], [-1, -2], [-3, -4]],
    columns=MultiIndex.from_tuples([["a", "b", "c"], ["d", "e", "f"]]),
    index=MultiIndex.from_tuples(
        [
            ["m1", "P3", 222],
            ["m1", "A5", 111],
            ["m2", "P3", 222],
            ["m2", "A5", 111],
        ],
        names=["i1", "i2", "i3"],
    ),
)
result = df.unstack(["i3", "i2"])
expected = df.unstack(["i3"]).unstack(["i2"])
tm.assert_frame_equal(result, expected)
