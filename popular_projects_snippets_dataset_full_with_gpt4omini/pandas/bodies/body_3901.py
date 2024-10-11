# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# PH 32624: Error when using a lot of indices to unstack.
# The error occurred only, if a lot of indices are used.
df = DataFrame(
    [[1]],
    columns=MultiIndex.from_tuples([[0]], names=["c1"]),
    index=MultiIndex.from_tuples(
        [[0, 0, 1, 0, 0, 0, 1]],
        names=["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
    ),
)
result = df.unstack(["i2", "i3", "i4", "i5", "i6", "i7"])
expected = DataFrame(
    [[1]],
    columns=MultiIndex.from_tuples(
        [[0, 0, 1, 0, 0, 0, 1]],
        names=["c1", "i2", "i3", "i4", "i5", "i6", "i7"],
    ),
    index=Index([0], name="i1"),
)
tm.assert_frame_equal(result, expected)
