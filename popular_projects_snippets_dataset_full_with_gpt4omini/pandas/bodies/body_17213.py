# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#48293
df = DataFrame({None: [1], "b": 2, "c": 3})

result = df.pivot(columns="b", index="c", values=None)
expected = DataFrame(
    1, index=Index([3], name="c"), columns=Index([2], name="b")
)
tm.assert_frame_equal(result, expected)

result = df.pivot(columns="b", values=None)
expected = DataFrame(1, index=[0], columns=Index([2], name="b"))
tm.assert_frame_equal(result, expected)
