# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#48293
df = DataFrame({None: [1], "b": 2, "c": 3})
result = df.pivot(columns=None)
expected = DataFrame({("b", 1): [2], ("c", 1): 3})
tm.assert_frame_equal(result, expected)

result = df.pivot(columns=None, index="b")
expected = DataFrame({("c", 1): 3}, index=Index([2], name="b"))
tm.assert_frame_equal(result, expected)

result = df.pivot(columns=None, index="b", values="c")
expected = DataFrame({1: 3}, index=Index([2], name="b"))
tm.assert_frame_equal(result, expected)
